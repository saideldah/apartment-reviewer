# Deal Metrics Calculator

A small, file-based real estate investment calculator. It reads apartment deal
data from a JSON file, calculates basic yield and financing metrics, and writes
the results to another JSON file.

No PDF extraction, no database, no frontend, no API — just the Python standard
library (`json`, `pathlib`).

## Requirements

- Python 3.8+
- No third-party packages

## Usage

Run from the **project root** (`apartment-reviewer/`):

```bash
# Uses the default deal directory: data/deals/putlitzstrasse-2a
python3 tools/deal_metrics/calculate_deal_metrics.py

# Or point it at any deal directory containing an input.json
python3 tools/deal_metrics/calculate_deal_metrics.py data/deals/some-other-deal
```

The tool:

1. Reads `<deal_dir>/input.json`
2. Validates that all required fields exist
3. Calculates the metrics
4. Writes `<deal_dir>/metrics.json` (money rounded to 2 decimals, yields to 4)
5. Prints a short summary to the terminal

## Input

The tool reads `input.json` from the given deal directory. All fields are
required:

```json
{
  "deal_id": "putlitzstrasse-2a-whg-21",
  "street": "Putlitzstraße",
  "house_number": "2a",
  "postal_code": "10551",
  "city": "Berlin",
  "state": "Berlin",
  "purchase_price": 294975,
  "living_space_sqm": 65.55,
  "cold_rent_monthly": 750,
  "non_recoverable_costs_yearly": 750,
  "renovation_budget": 25000,
  "vacant": true,
  "planned_rent_monthly": 1750,
  "interest_rate": 0.04,
  "repayment_rate": 0.015,
  "equity": 55000,
  "broker_fee_percent": 3.57,
  "notary_land_register_percent": 2.0,
  "property_transfer_tax_percent": 6.0,
  "target_yield": 0.04
}
```

| Field | Meaning |
|---|---|
| `deal_id` | Unique identifier for the deal |
| `street` | Street name |
| `house_number` | House number (string, e.g. `"2a"`) |
| `postal_code` | Postal code |
| `city` | City |
| `state` | State / federal state (Bundesland) |
| `purchase_price` | Purchase price in EUR |
| `living_space_sqm` | Living space in square meters |
| `cold_rent_monthly` | Current monthly cold rent (used if not vacant) |
| `non_recoverable_costs_yearly` | Yearly non-recoverable costs in EUR |
| `renovation_budget` | Planned renovation spend in EUR |
| `vacant` | `true` if vacant (uses planned rent) |
| `planned_rent_monthly` | Target monthly rent after letting |
| `interest_rate` | Annual loan interest rate (e.g. `0.04` = 4%) |
| `repayment_rate` | Annual repayment/amortization rate (e.g. `0.015`) |
| `equity` | Equity contributed in EUR |
| `broker_fee_percent` | Broker fee as % of purchase price |
| `notary_land_register_percent` | Notary + land registry as % of purchase price |
| `property_transfer_tax_percent` | Property transfer tax as % of purchase price |
| `target_yield` | Target gross yield (e.g. `0.04` = 4%) |

## Output

Writes `metrics.json` to the same deal directory:

```json
{
  "deal_id": "putlitzstrasse-2a-whg-21",
  "street": "Putlitzstraße",
  "house_number": "2a",
  "postal_code": "10551",
  "city": "Berlin",
  "state": "Berlin",
  "address": "Putlitzstraße 2a, 10551 Berlin, Berlin",
  "purchase_price_per_sqm": 4500.0,
  "acquisition_costs": 34128.61,
  "total_cost": 354103.61,
  "gross_yield": 0.0712,
  "net_yield": 0.0686,
  "loan_amount": 299103.61,
  "monthly_financing_payment": 1370.89,
  "monthly_rent_income": 1750,
  "monthly_non_recoverable_cost": 62.5,
  "monthly_cash_flow_before_tax": 316.61,
  "break_even_rent": 1433.39,
  "max_purchase_price_for_target_yield": 525000.0,
  "max_purchase_price_for_neutral_cash_flow": 356889.68
}
```

## Calculation rules

- **Rent used:** `planned_rent_monthly` if `vacant`, otherwise `cold_rent_monthly`.
- **Price per sqm:** `purchase_price / living_space_sqm`.
- **Acquisition costs:** sum of broker fee, notary/land register, and property
  transfer tax, each computed as `purchase_price * percent / 100`.
- **Total cost:** `purchase_price + acquisition_costs + renovation_budget`.
- **Gross yield:** `monthly_rent_income * 12 / purchase_price`.
- **Net yield:** `(monthly_rent_income * 12 - non_recoverable_costs_yearly) / purchase_price`.
- **Loan amount:** `total_cost - equity` (floored at `0`).
- **Monthly financing payment:** `loan_amount * (interest_rate + repayment_rate) / 12`.
- **Monthly cash flow before tax:** `monthly_rent_income - monthly_financing_payment - monthly_non_recoverable_cost`.
- **Break-even rent:** `monthly_financing_payment + monthly_non_recoverable_cost`.
- **Max purchase price for target yield:** `monthly_rent_income * 12 / target_yield`.
- **Max purchase price for neutral cash flow:** the price at which monthly cash
  flow is zero, given the rent, equity, renovation budget, financing rate, and
  acquisition cost percentages (floored at `0`).

## Notes

- The address is supplied as granular parts (`street`, `house_number`,
  `postal_code`, `city`, `state`). The output echoes those parts and adds a
  composed full `address` string for convenience.
- Each metric is implemented as its own small, pure function in
  `calculate_deal_metrics.py`, so individual formulas are easy to read and test.
- Money values are rounded to 2 decimals, yield values to 4 decimals.
- If a required field is missing, the tool prints an error listing the missing
  fields and exits with a non-zero status.
