from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def test_supplier_scorecard_and_recommendations_exist():
    scorecard = ROOT / "dashboards" / "supplier_scorecard.csv"
    recommendations = ROOT / "dashboards" / "computed_supplier_recommendations.csv"
    metrics = ROOT / "dashboards" / "optimization_metrics.json"
    assert scorecard.exists() and recommendations.exists() and metrics.exists()
    score = pd.read_csv(scorecard)
    recs = pd.read_csv(recommendations)
    summary = json.loads(metrics.read_text(encoding="utf-8"))
    assert len(score) > 0 and len(recs) > 0
    assert summary["items_analyzed"] == len(recs)
    assert score["average_unit_price"].gt(0).all()
