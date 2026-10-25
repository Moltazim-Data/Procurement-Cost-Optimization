"""Supplier/item price comparison for the synthetic procurement demo dataset."""
from pathlib import Path
import json
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def run_optimization():
    df=pd.read_csv(ROOT/"data/procurement_history.csv")
    item_col=next((c for c in ("item_name","item_description","item") if c in df.columns),None)
    supplier_col=next((c for c in ("supplier","supplier_name") if c in df.columns),None)
    price_col=next((c for c in ("unit_price","unit_price_eur","price") if c in df.columns),None)
    if not all((item_col,supplier_col,price_col)): raise ValueError("Procurement data needs item, supplier, and unit-price columns.")
    df[price_col]=pd.to_numeric(df[price_col],errors="coerce"); df=df.dropna(subset=[item_col,supplier_col,price_col]); df=df[df[price_col]>0]
    grouped=df.groupby([item_col,supplier_col]).agg(average_unit_price=(price_col,"mean"),purchases=(price_col,"size")).reset_index()
    if "quantity" in df.columns:
        qty=df.groupby([item_col,supplier_col])["quantity"].sum().rename("total_quantity").reset_index()
        grouped=grouped.merge(qty,on=[item_col,supplier_col],how="left")
    grouped["average_unit_price"]=grouped["average_unit_price"].round(2)
    grouped.to_csv(ROOT/"dashboards/supplier_scorecard.csv",index=False)
    recs=grouped.sort_values(["average_unit_price","purchases"]).groupby(item_col,as_index=False).first().rename(columns={supplier_col:"recommended_supplier"})
    recs.to_csv(ROOT/"dashboards/computed_supplier_recommendations.csv",index=False)
    summary={"purchase_rows_analyzed":int(len(df)),"items_analyzed":int(df[item_col].nunique()),"suppliers_analyzed":int(df[supplier_col].nunique()),"data_note":"Synthetic demo data; price-only recommendations require quote and quality validation."}
    (ROOT/"dashboards/optimization_metrics.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    report="# Procurement Cost Optimization — Computed Run\n\n> **Data note:** Synthetic demonstration data; these are not actual supplier quotes or realized savings.\n\n"
    report+=f"- Purchase rows analyzed: {summary['purchase_rows_analyzed']}\n- Distinct items analyzed: {summary['items_analyzed']}\n- Suppliers analyzed: {summary['suppliers_analyzed']}\n\n"
    report+="The scorecard summarizes average unit prices by item and supplier. The lowest observed average price is selected as a candidate without adjusting for freight, quality, lead time, minimum order quantity, or contract terms. Validate all recommendations before use.\n"
    (ROOT/"reports/cost_savings_report.md").write_text(report,encoding="utf-8")
    print(f"Optimization complete: {len(df)} purchase rows, {summary['items_analyzed']} items, {summary['suppliers_analyzed']} suppliers.")
    return summary
if __name__=="__main__": run_optimization()
