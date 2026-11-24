import os

expected_files = [
    'EDA_House_Prices/data/train.csv',
    'EDA_House_Prices/notebooks/House_Price_EDA.ipynb',
    'EDA_House_Prices/outputs/eda_dashboard.png',
    'EDA_House_Prices/outputs/correlation_heatmap.png',
    'EDA_House_Prices/outputs/saleprice_distribution.png',
    'EDA_House_Prices/outputs/outlier_analysis.png',
    'EDA_House_Prices/outputs/cleaned_dataset.csv',
    'EDA_House_Prices/outputs/descriptive_statistics.csv',
    'EDA_House_Prices/outputs/variable_classification_summary.csv',
    'EDA_House_Prices/outputs/outlier_comparison_summary.csv',
    'EDA_House_Prices/outputs/top3_features_correlation_covariance.csv',
    'EDA_House_Prices/outputs/eda_stats_summary.json',
    'EDA_House_Prices/outputs/other_visualizations/countplots_qual_style.png',
    'EDA_House_Prices/outputs/other_visualizations/missing_values_bar.png',
    'EDA_House_Prices/outputs/other_visualizations/pairplot_key_features.png',
    'EDA_House_Prices/outputs/other_visualizations/saleprice_by_neighborhood.png',
    'EDA_House_Prices/outputs/other_visualizations/saleprice_by_overallqual.png',
    'EDA_House_Prices/outputs/other_visualizations/scatter_key_features.png',
    'EDA_House_Prices/reports/EDA_Project_Report.pdf',
    'EDA_House_Prices/requirements.txt',
    'EDA_House_Prices/README.md'
]

print('=' * 85)
print('FINAL DELIVERABLES VERIFICATION AUDIT')
print('=' * 85)
all_ok = True
for f in expected_files:
    exists = os.path.exists(f)
    size = os.path.getsize(f) if exists else 0
    status = 'PASS' if exists and size > 0 else 'FAIL'
    print(f"[{status}] {f:<65} ({size:>10,} bytes)")
    if not (exists and size > 0):
        all_ok = False

print('=' * 85)
print(f"OVERALL STATUS: {'ALL DELIVERABLES VERIFIED SUCCESSFUL' if all_ok else 'VERIFICATION FAILED'}")
print('=' * 85)
