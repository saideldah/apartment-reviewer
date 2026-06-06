#!/usr/bin/env python3
"""File-based real estate investment calculator.

Reads apartment deal data from a JSON file, calculates yield and financing
metrics, and writes the results to another JSON file.

Each metric is computed by its own small, pure function so the formulas are
easy to read, test, and adjust independently.

Usage:
    python3 tools/deal_metrics/calculate_deal_metrics.py [deal_dir]

If no deal directory is given, defaults to data/deals/putlitzstrasse-2a.
"""

import json
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "deal_id",
    "street",
    "house_number",
    "postal_code",
    "city",
    "state",
    "purchase_price",
    "living_space_sqm",
    "cold_rent_monthly",
    "non_recoverable_costs_yearly",
    "renovation_budget",
    "vacant",
    "planned_rent_monthly",
    "interest_rate",
    "repayment_rate",
    "equity",
    "broker_fee_percent",
    "notary_land_register_percent",
    "property_transfer_tax_percent",
    "target_yield",
]


# --------------------------------------------------------------------------- #
# Equations — one function per metric                                         #
# --------------------------------------------------------------------------- #


def format_address(street, house_number, postal_code, city, state):
    """Compose a human-readable full address from its parts."""
    return f"{street} {house_number}, {postal_code} {city}, {state}"


def monthly_rent_income(planned_rent_monthly, cold_rent_monthly, vacant):
    """Planned rent if the apartment is vacant, otherwise current cold rent."""
    return planned_rent_monthly if vacant else cold_rent_monthly


def purchase_price_per_sqm(purchase_price, living_space_sqm):
    return purchase_price / living_space_sqm


def percent_of_price(purchase_price, percent):
    """A cost expressed as a percentage of the purchase price."""
    return purchase_price * percent / 100


def acquisition_costs(broker_fee, notary_land_register_cost, property_transfer_tax):
    return broker_fee + notary_land_register_cost + property_transfer_tax


def total_cost(purchase_price, acquisition_costs_value, renovation_budget):
    return purchase_price + acquisition_costs_value + renovation_budget


def gross_yield(monthly_rent_income_value, purchase_price):
    return monthly_rent_income_value * 12 / purchase_price


def net_yield(monthly_rent_income_value, non_recoverable_costs_yearly, purchase_price):
    return (
        (monthly_rent_income_value * 12) - non_recoverable_costs_yearly
    ) / purchase_price


def loan_amount(total_cost_value, equity):
    """Loan needed after equity, floored at zero."""
    return max(total_cost_value - equity, 0)


def monthly_financing_payment(loan_amount_value, interest_rate, repayment_rate):
    return loan_amount_value * (interest_rate + repayment_rate) / 12


def monthly_non_recoverable_cost(non_recoverable_costs_yearly):
    return non_recoverable_costs_yearly / 12


def monthly_cash_flow_before_tax(
    monthly_rent_income_value,
    monthly_financing_payment_value,
    monthly_non_recoverable_cost_value,
):
    return (
        monthly_rent_income_value
        - monthly_financing_payment_value
        - monthly_non_recoverable_cost_value
    )


def break_even_rent(monthly_financing_payment_value, monthly_non_recoverable_cost_value):
    return monthly_financing_payment_value + monthly_non_recoverable_cost_value


def max_purchase_price_for_target_yield(monthly_rent_income_value, target_yield):
    return monthly_rent_income_value * 12 / target_yield


def total_acquisition_percent(
    broker_fee_percent, notary_land_register_percent, property_transfer_tax_percent
):
    return (
        broker_fee_percent
        + notary_land_register_percent
        + property_transfer_tax_percent
    ) / 100


def max_loan_supported(
    monthly_rent_income_value,
    monthly_non_recoverable_cost_value,
    interest_rate,
    repayment_rate,
):
    """Largest loan whose annual debt service the net rent can cover."""
    monthly_available_for_financing = (
        monthly_rent_income_value - monthly_non_recoverable_cost_value
    )
    annual_debt_service_rate = interest_rate + repayment_rate
    return monthly_available_for_financing * 12 / annual_debt_service_rate


def max_purchase_price_for_neutral_cash_flow(
    max_loan_supported_value, equity, renovation_budget, total_acquisition_percent_value
):
    """Purchase price at which monthly cash flow is zero, floored at zero."""
    price = (max_loan_supported_value + equity - renovation_budget) / (
        1 + total_acquisition_percent_value
    )
    return max(price, 0)


# --------------------------------------------------------------------------- #
# Orchestration                                                               #
# --------------------------------------------------------------------------- #


def validate(data):
    """Raise ValueError if any required field is missing."""
    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")


def build_metrics(data):
    """Compute every metric by composing the equation functions above."""
    rent = monthly_rent_income(
        data["planned_rent_monthly"], data["cold_rent_monthly"], data["vacant"]
    )

    broker_fee = percent_of_price(data["purchase_price"], data["broker_fee_percent"])
    notary_cost = percent_of_price(
        data["purchase_price"], data["notary_land_register_percent"]
    )
    transfer_tax = percent_of_price(
        data["purchase_price"], data["property_transfer_tax_percent"]
    )
    acquisition = acquisition_costs(broker_fee, notary_cost, transfer_tax)

    total = total_cost(data["purchase_price"], acquisition, data["renovation_budget"])
    loan = loan_amount(total, data["equity"])

    financing_payment = monthly_financing_payment(
        loan, data["interest_rate"], data["repayment_rate"]
    )
    non_recoverable_monthly = monthly_non_recoverable_cost(
        data["non_recoverable_costs_yearly"]
    )

    acquisition_percent = total_acquisition_percent(
        data["broker_fee_percent"],
        data["notary_land_register_percent"],
        data["property_transfer_tax_percent"],
    )
    supported_loan = max_loan_supported(
        rent, non_recoverable_monthly, data["interest_rate"], data["repayment_rate"]
    )

    return {
        "deal_id": data["deal_id"],
        "street": data["street"],
        "house_number": data["house_number"],
        "postal_code": data["postal_code"],
        "city": data["city"],
        "state": data["state"],
        "address": format_address(
            data["street"],
            data["house_number"],
            data["postal_code"],
            data["city"],
            data["state"],
        ),
        "purchase_price_per_sqm": round(
            purchase_price_per_sqm(data["purchase_price"], data["living_space_sqm"]), 2
        ),
        "acquisition_costs": round(acquisition, 2),
        "total_cost": round(total, 2),
        "gross_yield": round(gross_yield(rent, data["purchase_price"]), 4),
        "net_yield": round(
            net_yield(
                rent, data["non_recoverable_costs_yearly"], data["purchase_price"]
            ),
            4,
        ),
        "loan_amount": round(loan, 2),
        "monthly_financing_payment": round(financing_payment, 2),
        "monthly_rent_income": rent,
        "monthly_non_recoverable_cost": round(non_recoverable_monthly, 2),
        "monthly_cash_flow_before_tax": round(
            monthly_cash_flow_before_tax(
                rent, financing_payment, non_recoverable_monthly
            ),
            2,
        ),
        "break_even_rent": round(
            break_even_rent(financing_payment, non_recoverable_monthly), 2
        ),
        "max_purchase_price_for_target_yield": round(
            max_purchase_price_for_target_yield(rent, data["target_yield"]), 2
        ),
        "max_purchase_price_for_neutral_cash_flow": round(
            max_purchase_price_for_neutral_cash_flow(
                supported_loan,
                data["equity"],
                data["renovation_budget"],
                acquisition_percent,
            ),
            2,
        ),
    }


def print_summary(metrics):
    """Print a short human-readable summary to the terminal."""
    print(f"Deal:    {metrics['deal_id']}")
    print(f"Address: {metrics['address']}")
    print("-" * 48)
    print(f"  Price per sqm:          {metrics['purchase_price_per_sqm']:>12,.2f} EUR")
    print(f"  Total cost:             {metrics['total_cost']:>12,.2f} EUR")
    print(f"  Loan amount:            {metrics['loan_amount']:>12,.2f} EUR")
    print(f"  Gross yield:            {metrics['gross_yield'] * 100:>11.2f} %")
    print(f"  Net yield:              {metrics['net_yield'] * 100:>11.2f} %")
    print(f"  Monthly rent income:    {metrics['monthly_rent_income']:>12,.2f} EUR")
    print(f"  Monthly financing:      {metrics['monthly_financing_payment']:>12,.2f} EUR")
    print(f"  Monthly cash flow:      {metrics['monthly_cash_flow_before_tax']:>12,.2f} EUR")
    print(f"  Break-even rent:        {metrics['break_even_rent']:>12,.2f} EUR")


def main():
    deal_dir = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else Path("data/deals/putlitzstrasse-2a")
    )
    input_path = deal_dir / "input.json"
    output_path = deal_dir / "metrics.json"

    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(input_path.read_text(encoding="utf-8"))

    try:
        validate(data)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    metrics = build_metrics(data)

    output_path.write_text(
        json.dumps(metrics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print_summary(metrics)
    print("-" * 48)
    print(f"Wrote metrics to {output_path}")


if __name__ == "__main__":
    main()
