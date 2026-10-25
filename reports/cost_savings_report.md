# Procurement Cost Optimization — Demo Dataset Review

> **Data note:** This report uses synthetic demonstration data. It does not represent actual supplier quotations or realized savings.

## Dataset profile
- Purchase rows: 120
- Distinct items: 12
- Distinct suppliers: 4
- Price currency in the source data: USD

## Analysis approach
The optimization script groups historical records by item and supplier, calculates average unit prices, and selects the lowest observed average as a candidate recommendation. It writes a supplier scorecard and computed recommendations to the dashboard folder.

## Important limitations
The included illustrative recommendation and benchmark CSVs are demonstration artifacts; they are not verified against external supplier quotations. The basic price-only model does not account for freight, lead time, quality, minimum order quantities, payment terms, or contract commitments. Do not use its recommendations for purchasing decisions without validating those factors.

## Recommended next steps
1. Run `python scripts/optimization_model.py` from the repository root.
2. Review `dashboards/supplier_scorecard.csv` and `dashboards/computed_supplier_recommendations.csv`.
3. Replace generated data with approved procurement records and current supplier quotes.
4. Re-run the model and document realized savings only after purchases are completed.
