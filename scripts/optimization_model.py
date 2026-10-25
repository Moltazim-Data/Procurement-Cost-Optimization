import pandas as pd
import numpy as np

def run_optimization():
    df = pd.read_csv("data/procurement_history.csv")
    scorecard = df.groupby(['supplier_name', 'item_description']).agg({
        'unit_price_eur': 'mean',
        'lead_time_days': 'mean',
        'defect_rate': 'mean'
    }).reset_index()
    print("Optimization Analysis Complete.")

if __name__ == "__main__":
    run_optimization()
