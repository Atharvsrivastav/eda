# Exploratory Data Analysis of House Prices

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Project Type](https://img.shields.io/badge/Project-Exploratory%20Data%20Analysis%20(EDA)-green.svg)]()
[![Dataset](https://img.shields.io/badge/Dataset-Ames%20Housing%20(Kaggle)-orange.svg)](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
[![Academic Status](https://img.shields.io/badge/Status-University%20Level%20Submission-purple.svg)]()

A comprehensive, university-level Exploratory Data Analysis (EDA) project investigating the physical, structural, temporal, and spatial determinants of residential house prices using the Ames Housing Dataset.

> **Project Mandate:** This project focuses exclusively on **Exploratory Data Analysis (EDA)**. In strict compliance with the academic brief, no machine learning, regression modeling, predictive algorithms, or artificial intelligence models are deployed. All conclusions are derived through empirical descriptive statistics, parametric and non-parametric hypothesis checks, and publication-quality data visualizations.

---

## Deliverables Directory: `EDA_House_Prices/`

The complete deliverable directory structure is located in [`EDA_House_Prices/`](./EDA_House_Prices/):

```text
EDA_House_Prices/
│
├── data/
│   └── train.csv                               # Original Ames Housing Dataset (1,460 rows × 81 columns)
│
├── notebooks/
│   └── House_Price_EDA.ipynb                   # Fully executed, university-grade Jupyter Notebook (54 cells)
│
├── outputs/
│   ├── eda_dashboard.png                       # High-resolution 2×2 Executive Summary Dashboard (300 DPI)
│   ├── correlation_heatmap.png                 # Masked coolwarm correlation heatmap of top 10 features
│   ├── saleprice_distribution.png              # Target distribution: Raw Hist+KDE, Boxplot, Log(SalePrice)
│   ├── outlier_analysis.png                    # Outlier diagnosis: Boxplot & Dual-Method Scatter comparison
│   ├── cleaned_dataset.csv                     # Authoritative cleaned dataset (zero missing values)
│   ├── descriptive_statistics.csv              # Full parametric & non-parametric summary table
│   ├── variable_classification_summary.csv     # Complete 81-column taxonomy breakdown
│   ├── outlier_comparison_summary.csv          # IQR vs. Z-Score detection rate comparison
│   ├── eda_stats_summary.json                  # Machine-readable factual metrics dictionary
│   │
│   └── other_visualizations/
│       ├── countplots_qual_style.png           # Frequency counts for OverallQual and HouseStyle
│       ├── missing_values_bar.png              # Bar chart of top missing value percentages
│       ├── pairplot_key_features.png           # 5-variable multivariate pairplot with diagonal KDE
│       ├── saleprice_by_neighborhood.png       # Boxplot of SalePrice by Neighborhood (sorted by median)
│       ├── saleprice_by_overallqual.png        # Boxplot of SalePrice across OverallQual ratings (1–10)
│       └── scatter_key_features.png            # Bivariate scatter: GrLivArea, TotalBsmtSF, YearBuilt
│
├── reports/
│   └── EDA_Project_Report.pdf                  # 8-page publication-grade Academic Project Report
│
├── requirements.txt                            # Pinned Python package dependencies
└── README.md                                   # Comprehensive academic documentation
```

For full documentation, research findings, and defense guide, please refer to [EDA_House_Prices/README.md](./EDA_House_Prices/README.md).
