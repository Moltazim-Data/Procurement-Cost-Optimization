# Procurement Cost Optimization


> **Demo data notice:** Procurement history, supplier recommendations, benchmarks, and chart assets added for this repository are synthetic examples. They are not real supplier quotes or realized savings.

Python-based procurement analytics for comparing supplier and item pricing, lead times, and defect rates.

## Project contents
- `scripts/optimization_model.py` — supplier/item scorecard workflow
- `data/procurement_history.csv` — purchase-order history
- `dashboards/` — benchmark outputs and dashboard
- `reports/` — cost analysis summary

## Run
```bash
pip install -r requirements.txt
python scripts/optimization_model.py
```

**Scope note:** The current script summarizes supplier/item metrics; it does not implement a complete constrained optimization or validated savings simulation.
