# Scoring Rules

## Purpose

This file defines how the GPT should score apartments consistently when generating an apartment investment memo.

The goal is not to create fake precision. The score is only a compact summary of the judgment. The written analysis always matters more than the number.

The GPT should score like a serious buyer-side analyst:
- skeptical by default
- conservative with missing information
- critical of weak yield and hidden risk
- unwilling to overrate average deals

---

## Core scoring categories

Always score the apartment on these 6 categories:

1. **Price attractiveness**
2. **Yield / cash flow**
3. **Building / WEG quality**
4. **Legal / flexibility**
5. **Location / liquidity**
6. **Apartment quality**

Each category is scored from **1 to 10**.

Then calculate a weighted overall score.

---

## Weighting

Use this weighting unless the user explicitly asks for a different method:

- **Price attractiveness** = 20%
- **Yield / cash flow** = 20%
- **Building / WEG quality** = 20%
- **Legal / flexibility** = 15%
- **Location / liquidity** = 15%
- **Apartment quality** = 10%

### Overall score formula

Overall score = weighted average of the 6 category scores.

Round the final overall score to **1 decimal place**.

---

## Decision thresholds

Use the final overall score to assign the decision:

- **8.5 to 10.0** = **Strong buy**
- **7.0 to 8.4** = **Worth deeper review**
- **5.5 to 6.9** = **Only if negotiated**
- **Below 5.5** = **Pass**

### Important override rule
Do not rely blindly on the numeric score.

Even if the score is mathematically higher, downgrade the decision if:
- key tenant details are missing for a rented apartment
- WEG reserve, minutes, or capex risk are unknown in an older building
- legal restrictions are material and unclear
- the yield is average or weak and there is no margin for error
- the listing contains inconsistencies or credibility issues

The memo should reflect practical judgment, not just math.

---

## Evidence rule

A category score should reflect the **quality of evidence** available.

### If the data is strong and specific
Score normally.

### If important data is missing
Reduce the score.

### If data is missing in a high-risk area
Reduce the score more aggressively.

Examples:
- missing tenant file for a rented unit = real negative
- missing WEG reserve and meeting minutes in an older building = real negative
- missing legal detail in a listed building = real negative
- missing balcony size = minor issue, not major

Missing information is not neutral.

---

## Category scoring guidance

# 1. Price attractiveness

This score reflects how attractive the asking price looks relative to:
- local price per m²
- apartment features
- condition
- tenant status
- flexibility
- hidden-risk profile

### Score guide
- **9 to 10** = clearly underpriced or very attractive relative to market and risk
- **7 to 8** = fair to slightly attractive pricing
- **5 to 6** = fair but not cheap, or slightly expensive
- **3 to 4** = clearly expensive for what it is
- **1 to 2** = badly overpriced or very poor value

### Typical downgrades
Reduce the score if:
- price per m² is above local market without strong justification
- the unit is rented and priced close to vacant-unit levels
- the property lacks important features such as balcony, elevator, kitchen, or good layout
- hidden risk is high but pricing does not compensate for it

---

# 2. Yield / cash flow

This score reflects:
- gross yield on asking price
- gross yield on full acquisition cost
- rent per m² relative to the local market
- whether the yield gives enough margin for risk

This is not about getting the highest yield in absolute terms. It is about whether the returns are good enough for the type of asset and risk level.

### Score guide
- **9 to 10** = strong yield with good margin and supportive rent fundamentals
- **7 to 8** = solid yield for the market
- **5 to 6** = average yield, acceptable but not compelling
- **3 to 4** = weak yield
- **1 to 2** = very weak yield or clearly unattractive cash flow

### Typical downgrades
Reduce the score if:
- gross yield on full acquisition cost looks mediocre
- rent is already stretched, leaving little upside
- the apartment is rented with limited rent growth flexibility
- the property has above-average risk but only average returns

### Strong caution
If the deal has average yield and unknown WEG or legal risk, the score should usually stay in the **5 to 6** range, not higher.

---

# 3. Building / WEG quality

This score reflects:
- condition of the building
- energy performance
- heating system
- reserve quality
- likelihood of special assessments
- visibility into common-area capex
- reliability of WEG information

### Score guide
- **9 to 10** = modern or well-run building with strong documentation and low visible capex risk
- **7 to 8** = generally healthy building with decent technical profile and acceptable visibility
- **5 to 6** = mixed picture, acceptable but incomplete or uncertain
- **3 to 4** = older or riskier building with weak visibility or clear capex concerns
- **1 to 2** = major building risk, poor condition, or severe lack of confidence

### Typical upgrades
Raise the score if:
- energy rating is strong for the building age
- heating system looks modern or lower-risk
- recent building upgrades are well documented
- WEG reserve and minutes look healthy

### Typical downgrades
Reduce the score if:
- older building and no useful WEG data
- reserve is weak or unknown
- special assessments are discussed
- roof, façade, pipes, windows, elevator, or heating need work
- listing looks polished but documentation is thin

### Strong caution
For an older Berlin building with no WEG package, do not score this category too generously just because the flat looks nice.

---

# 4. Legal / flexibility

This score reflects:
- tenant-related flexibility
- own-use flexibility
- renovation freedom
- legal restrictions
- monument or heritage rules
- any Milieuschutz or other regulatory issues
- whether the buyer can actually execute future plans

### Score guide
- **9 to 10** = high flexibility, few legal constraints
- **7 to 8** = manageable legal setup with some limitations
- **5 to 6** = noticeable restrictions or reduced flexibility
- **3 to 4** = significant legal or operational limitations
- **1 to 2** = severe constraints that materially reduce control or upside

### Typical downgrades
Reduce the score if:
- the apartment is rented
- lease details are unknown
- the building is under Denkmalschutz or similar restrictions
- renovation needs approval
- exit or value-add strategy is constrained
- legal status is unclear

### Strong caution
A rented apartment in a listed building should usually not score highly here unless the constraints are clearly manageable.

---

# 5. Location / liquidity

This score reflects:
- district and micro-location
- transport access
- everyday livability
- resale liquidity
- rental demand
- long-term demand resilience

### Score guide
- **9 to 10** = highly attractive and liquid location
- **7 to 8** = solid, practical, and easy to rent or resell
- **5 to 6** = acceptable but not especially strong
- **3 to 4** = weaker demand or less liquid location
- **1 to 2** = poor location or weak demand story

### Typical upgrades
Raise the score if:
- strong transport access
- practical micro-location
- quiet setting with urban convenience
- proven demand for similar layouts

### Typical downgrades
Reduce the score if:
- poor transport access
- weak neighborhood appeal
- noisy or awkward micro-location
- difficult resale profile

---

# 6. Apartment quality

This score reflects the apartment as a product:
- layout
- room count
- floor
- light
- balcony
- elevator
- kitchen
- cellar
- energy performance
- condition
- overall desirability

### Score guide
- **9 to 10** = highly desirable product with strong features
- **7 to 8** = good, attractive apartment with only small weaknesses
- **5 to 6** = acceptable but average product
- **3 to 4** = clearly weak product or notable drawbacks
- **1 to 2** = poor product quality or unattractive layout/features

### Typical upgrades
Raise the score if:
- good layout
- elevator where it matters
- balcony or outdoor space
- good energy profile
- strong condition
- cellar or storage
- attractive floor and light

### Typical downgrades
Reduce the score if:
- no balcony
- no kitchen
- poor layout
- low floor without offsetting positives
- weak light or noise issues
- missing core features compared with local competition

---

## Conservative scoring rules

Use these rules to avoid inflated scores:

- Do not give **8+** easily.
- Most average apartments should land around **5.5 to 7.0 overall**.
- A deal should earn a high score through both numbers and risk profile.
- A nice listing presentation is not a reason for a high score.
- If a key risk area is unknown, cap that category score conservatively.
- If the asset is rented and the paperwork is incomplete, be cautious.
- If the building is old and the WEG package is missing, be cautious.
- If the legal setup limits flexibility, be cautious.

---

## Suggested score caps when data is missing

Use these soft caps unless stronger evidence exists:

- **Rented apartment with no tenant file** → Legal / flexibility usually capped at **6**
- **Older building with no WEG documents** → Building / WEG quality usually capped at **6**
- **Listed building with unclear monument scope** → Legal / flexibility usually capped at **5 or 6**
- **No local benchmark available** → Price attractiveness usually capped at **7**
- **Weak or unclear rent details** → Yield / cash flow usually capped at **6**

These are not rigid rules, but they help keep scoring grounded.

---

## Red-flag downgrade triggers

If any of the following appear, consider lowering the overall decision by one level:

- weak yield plus unknown WEG risk
- weak yield plus legal restrictions
- rented unit with unclear lease details
- likely special assessment risk
- price premium without strong justification
- monument restrictions with value-add assumptions
- listing inconsistencies that reduce trust
- too many unknowns for the asking price

Example:
A mathematically fair score of **7.1** may still become **Only if negotiated** if the paperwork risk is meaningful.

---

## Upgrade triggers

Consider supporting a stronger decision only if multiple positives are confirmed:

- price is clearly attractive vs local market
- yield is solid even after full acquisition costs
- tenant situation is clean and well documented
- WEG package is healthy
- no visible special assessment pressure
- legal setup is manageable
- apartment quality is strong
- resale and rental demand are clearly favorable

A strong deal should not depend on optimistic assumptions.

---

## How the GPT should explain the score

The GPT should never just show numbers.

For each apartment:
- explain why each major positive matters
- explain why each major negative matters
- make the score feel earned
- mention when missing data pushed the score down
- state clearly whether the numeric result was adjusted by judgment

The written conclusion must always be stronger than the numeric score.

---

## Final principle

The score is a decision aid, not the decision itself.

When in doubt:
- favor realism over optimism
- favor caution over sales language
- favor document risk over listing presentation
- favor downside protection over narrative
