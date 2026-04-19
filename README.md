# Apartment Reviewer

This repository is a document-driven system for producing consistent Berlin apartment investment memos.

It combines:
- a fixed memo structure
- scoring and decision rules
- calculation rules for acquisition cost and yield
- style and tone guidance
- Berlin and Germany market context
- an example reference report

The intent is to review an apartment listing or document package and produce a skeptical, decision-oriented memo rather than a generic summary.

## Repository Contents

- `Apartment Memo Template.md`: canonical output structure and section order
- `Scoring Rules.md`: score logic, weighting, caps, and decision thresholds
- `Calculation Rules.md`: acquisition cost and yield assumptions
- `Style Rules.md`: tone, formatting, and writing standards
- `Extended GPT Operating Rules.md`: handling for rented units, old buildings, missing data, and verification
- `Berlin & Germany Market Facts and Sources.md`: benchmark context and source hierarchy
- `Reference Apartment Report.md`: example of target quality and finish
- `Knowledge File Usage Guide.md`: orchestration guide that defines file priority and workflow
- `berlin_rental_property_notes.md`: working notes and domain context

## Recommended Workflow

1. Gather the available inputs.
   Supported inputs can include listing links, listing text, screenshots, PDF exposés, tenant details, WEG documents, and user notes.
2. Lock the output shape with `Apartment Memo Template.md`.
3. Compute acquisition costs, rent metrics, and yield using `Calculation Rules.md`.
4. Score the deal conservatively using `Scoring Rules.md`.
5. Apply the tone and formatting rules from `Style Rules.md`.
6. Use `Extended GPT Operating Rules.md` for missing data, rented-unit logic, and verification requirements.
7. Use `Berlin & Germany Market Facts and Sources.md` for contextual claims and benchmarks.
8. Use `Reference Apartment Report.md` as a final quality check.

## File Priority

When files overlap, use this order:

1. `Apartment Memo Template.md`
2. `Scoring Rules.md`
3. `Calculation Rules.md`
4. `Style Rules.md`
5. `Extended GPT Operating Rules.md`
6. `Berlin & Germany Market Facts and Sources.md`
7. `Reference Apartment Report.md`

## Expected Output

The target output is an apartment investment memo with:
- an executive scorecard
- a clear buy / negotiate / pass recommendation
- explicit investment math
- a risk-focused assessment of tenant, WEG, legal, and building issues
- clear separation of confirmed facts, assumptions, and missing information
- a short list of the highest-priority follow-up documents to request

## Notes

- Missing data should not be treated as neutral.
- Hidden downside should be reflected in lower confidence and lower scores where appropriate.
- The system is optimized for Berlin residential apartment analysis and uses Berlin-specific acquisition-cost and market context.
