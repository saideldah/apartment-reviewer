# Calculation Rules

## Purpose
Use these rules to keep apartment reports financially consistent.
Always use exact listing data when available. Use the defaults below only when the listing or user has not provided a better number.

## Scope
These rules are designed for apartment analysis in Berlin and Germany.
They are for quick underwriting and screening, not for tax, legal, or financing advice.

## 1. Core purchase cost assumptions

### 1.1 Purchase price
- Use the asking price from the listing unless the user gives a negotiated price.
- If a price range exists, use the current asking price and mention the range separately.

### 1.2 Berlin property transfer tax
- Default assumption for Berlin: **6.0%** of the taxable purchase price.
- Formula:
  - `property transfer tax = purchase price x 0.06`
- Use the property location to determine the tax rate. If the apartment is not in Berlin, do not use 6.0% by default.

### 1.3 Notary and land registry
- Default assumption: **2.0%** of purchase price.
- Formula:
  - `notary + land registry = purchase price x 0.02`
- Use 2.0% for quick screening unless the user provides a more precise figure.
- If a more conservative or tighter estimate is needed, mention that real-life costs often land around 1.5% to 2.0%.

### 1.4 Broker fee handling
- If the listing clearly states a buyer broker fee, use it exactly.
- If the listing says **provisionsfrei**, use **0%**.
- If the listing does not state any buyer broker fee, do **not** invent one as a fact.
- In that case:
  - mark the broker fee as **not provided**, and
  - either exclude it from the base case, or
  - show an optional sensitivity scenario if the user wants a conservative estimate.
- Formula:
  - `broker fee = purchase price x buyer broker fee rate`

### 1.5 Total acquisition cost
Include only clearly required acquisition costs unless the user asks for a more complete ownership model.

**Base formula:**
- `total acquisition cost = purchase price + property transfer tax + notary/land registry + buyer broker fee`

Do **not** include the following in the base total unless the user explicitly asks:
- renovation budget
- furniture or fitted kitchen cost
- financing costs
- mortgage setup fees
- ongoing operating costs
- vacancy assumptions
- maintenance reserve assumptions outside the stated purchase costs

## 2. Price and rent calculations

### 2.1 Price per m²
- Formula:
  - `price per m² = purchase price / living area`
- Use living area, not plot size.
- If living area is missing or unclear, say so explicitly.

### 2.2 Monthly rent
- Prefer **current monthly Kaltmiete**.
- If the listing only shows rent without saying whether it is warm or cold, label it as **rent type not confirmed**.
- Do not silently assume warm rent is Kaltmiete.

### 2.3 Annual rent
- Formula:
  - `annual rent = monthly rent x 12`

### 2.4 Rent per m² per month
- Formula:
  - `rent per m² per month = monthly rent / living area`

## 3. Yield formulas

### 3.1 Gross yield on asking price
- Formula:
  - `gross yield on asking price = annual rent / purchase price`
- Show as a percentage.

### 3.2 Gross yield on total acquisition cost
- Formula:
  - `gross yield on total acquisition cost = annual rent / total acquisition cost`
- Show as a percentage.

### 3.3 Net yield
- Do **not** calculate net yield unless enough data is available.
- Net yield should only be shown if at least the following are known or explicitly assumed:
  - non-allocable Hausgeld
  - expected maintenance burden
  - vacancy assumption if relevant
  - property tax if relevant
  - management cost if relevant

## 4. Hausgeld handling

- Always show the listed Hausgeld separately.
- Do not subtract Hausgeld from rent in the main gross yield calculation.
- If the non-allocable owner portion is known, mention it separately.
- If only total Hausgeld is known, say that the breakdown is missing and avoid pretending the full amount is owner cost.

## 5. Local market comparison rules

### 5.1 Price premium or discount vs local benchmark
- Formula:
  - `price premium or discount % = ((subject price per m² / local average price per m²) - 1) x 100`

### 5.2 Rent premium or discount vs local benchmark
- Formula:
  - `rent premium or discount % = ((subject rent per m² / local average rent per m²) - 1) x 100`

### 5.3 Benchmark interpretation
Use these ranges unless the user prefers a different scale:
- within about **3%** of benchmark = roughly fair
- about **3% to 8% above** benchmark = slightly expensive
- more than about **8% above** benchmark = clearly expensive
- about **3% to 8% below** benchmark = slightly cheap
- more than about **8% below** benchmark = clearly cheap

Do not judge on benchmark alone. Features such as balcony, floor, elevator, condition, energy class, tenancy status, and micro-location can justify a premium or discount.

## 6. Missing data rules

- If a number is missing, say it is missing.
- If a number is estimated, label it as an assumption.
- If rent type is unclear, say so.
- If broker fee is unclear, do not treat a guess as a fact.
- If key documents are missing, treat that as risk, not as neutral missing information.

## 7. Rounding and presentation rules

- Round percentages to **2 decimal places**.
- Round price per m² and rent per m² to **2 decimal places**.
- Keep euro amounts in full where useful.
- If the source provides cents, keep cents for rent.
- For summary tables, whole euros are fine if they improve readability.

## 8. Default interpretation rules

### Strong vs weak numbers
Use this only as a rough screening guide, not as a law:

#### Gross yield on asking price
- below **3.0%** = weak
- **3.0% to 4.0%** = weak to average
- **4.0% to 5.0%** = decent
- above **5.0%** = strong for a simple first-pass screen

#### Gross yield on total acquisition cost
- below **3.0%** = weak
- **3.0% to 3.75%** = average at best
- **3.75% to 4.5%** = decent
- above **4.5%** = strong for a simple first-pass screen

Always adjust judgment for:
- location quality
- tenant risk
- WEG risk
- legal restrictions
- energy performance
- future capex risk

## 9. Conservative analysis rules

When data is incomplete:
- lean conservative
- avoid inflating upside
- do not assume easy rent increases
- do not assume zero capex risk in older buildings
- do not treat a high listed rent as sustainable until the lease details confirm it

## 10. Standard formulas block

Use this exact block when helpful:

```text
purchase price = asking price
property transfer tax = purchase price x 0.06
notary + land registry = purchase price x 0.02
broker fee = purchase price x buyer broker fee rate

total acquisition cost = purchase price + property transfer tax + notary + land registry + broker fee

price per m² = purchase price / living area
annual rent = monthly rent x 12
rent per m² per month = monthly rent / living area

gross yield on asking price = annual rent / purchase price
gross yield on total acquisition cost = annual rent / total acquisition cost
```
