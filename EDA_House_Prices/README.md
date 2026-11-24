# Exploratory Data Analysis of House Prices

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Project Type](https://img.shields.io/badge/Project-Exploratory%20Data%20Analysis%20(EDA)-green.svg)]()
[![Dataset](https://img.shields.io/badge/Dataset-Ames%20Housing%20(Kaggle)-orange.svg)](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
[![Academic Status](https://img.shields.io/badge/Status-University%20Level%20Submission-purple.svg)]()

A comprehensive, university-level Exploratory Data Analysis (EDA) project investigating the physical, structural, temporal, and spatial determinants of residential house prices using the Ames Housing Dataset.

> **Project Mandate:** This project focuses exclusively on **Exploratory Data Analysis (EDA)**. In strict compliance with the academic brief, no machine learning, regression modeling, predictive algorithms, or artificial intelligence models are deployed. All conclusions are derived through empirical descriptive statistics, parametric and non-parametric hypothesis checks, and publication-quality data visualizations.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Problem Statement & Guiding Questions](#problem-statement--guiding-questions)
3. [Dataset Description & Sourcing](#dataset-description--sourcing)
4. [Technology Stack](#technology-stack)
5. [Directory & Deliverables Structure](#directory--deliverables-structure)
6. [Installation & Setup Instructions](#installation--setup-instructions)
7. [How to Execute the Notebook](#how-to-execute-the-notebook)
8. [The 10-Step EDA Methodology](#the-10-step-eda-methodology)
9. [Key Analytical Findings & Empirical Insights](#key-analytical-findings--empirical-insights)
10. [Academic Viva Voce & Defense Guide](#academic-viva-voce--defense-guide)
11. [Limitations & Future Scope](#limitations--future-scope)

---

## 1. Project Overview

In real estate economics, residential property pricing is governed by a complex web of structural dimensions, physical land characteristics, craftsmanship tiers, and geographic location premiums. Before applying inductive predictive models, empirical data science demands a rigorous exploratory audit to diagnose distributions, measure collinearity, inspect anomalies, and treat domain-specific missingness.

This project delivers a complete, end-to-end analytical investigation of the Ames Housing dataset (`train.csv`), spanning:
- Descriptive statistical profiling across continuous, discrete, nominal, and ordinal scales.
- Distributional diagnosis and logarithmic variance stabilization of `SalePrice`.
- Pearson linear correlation and Spearman rank-order correlation analysis.
- Bivariate and multivariate visual projections.
- Dual-method outlier detection (Tukey's IQR vs. Parametric $Z$-Score).
- Domain-driven data quality sanitization (differentiating feature absence from unrecorded data).
- A unified 2×2 Executive Exploratory Data Analysis Dashboard.

---

## 2. Problem Statement & Guiding Questions

### Problem Statement
Real estate transactions in municipal submarkets are characterized by heavy right-skewed price distributions, spatial disparities, and high dimensional interactions. Without a principled exploratory foundation, raw transactional records can mislead analysts and policy-makers.

### Core Guiding Questions
1. **Target Distribution:** How is `SalePrice` distributed across Ames? What are its mean, median, skewness, and kurtosis?
2. **Correlation Matrix:** Which numerical attributes correlate most strongly with property transaction value?
3. **Quality Monotonicity:** Does overall material and finish quality (`OverallQual`) translate into an ordered price premium?
4. **Spatial Segmentation:** Do certain Ames neighborhoods exhibit statistically distinct pricing premiums?
5. **Outlier Identification:** Are extreme records measurement errors, or do they represent genuine luxury or atypical market transfers?
6. **Structural Missingness:** Which columns exhibit missing values, and which among them denote absent physical amenities rather than lost data?

---

## 3. Dataset Description & Sourcing

* **Dataset Name:** Ames Housing Dataset: Advanced Regression Techniques (`train.csv`).
* **Author / Provenance:** Compiled by Professor Dean De Cock (Truman State University) as a modern replacement for the classic Boston Housing dataset.
* **Source:** [Kaggle Competition: House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
* **Dataset Shape:** Exactly **1,460 observations (rows)** and **81 features (columns)**.
* **Target Variable:** `SalePrice` (Continuous monetary value in USD).
* **Attribute Types:** 33 numerical attributes, 43 categorical/nominal attributes, and 16 ordinal scales.

---

## 4. Technology Stack

| Technology | Role & Version | Purpose |
| :--- | :--- | :--- |
| **Python** | 3.10+ (Tested on 3.12) | Core scientific programming language |
| **Pandas** | `>=2.0.0` | Dataframe manipulation, aggregation, and categorical encoding |
| **NumPy** | `>=1.24.0` | High-performance vector operations and array math |
| **Matplotlib** | `>=3.7.0` | Foundational graphing, line plots, and 2×2 dashboard layout |
| **Seaborn** | `>=0.12.0` | Statistical visualization, KDE densities, boxplots, pairplots, and heatmaps |
| **SciPy** | `>=1.10.0` | Higher-order statistical moments (skewness, kurtosis, $z$-score distributions) |
| **ReportLab** | `>=4.0.0` | Automated generation of the 8-page academic PDF report |
| **Jupyter / nbformat** | `>=5.9.0` | Executable interactive notebook presentation (`.ipynb`) |

---

## 5. Directory & Deliverables Structure

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

---

## 6. Installation & Setup Instructions

### Step 1: Clone or Open the Workspace
```bash
git clone <repository-url>
cd EDA_House_Prices
```

### Step 2: Create and Activate a Python Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

---

## 7. How to Execute the Notebook

You can interact with and re-run the complete Jupyter Notebook using your preferred interface:

### Option A: Using Jupyter Lab / Jupyter Notebook
```bash
jupyter notebook notebooks/House_Price_EDA.ipynb
```

### Option B: Using VS Code
1. Open the project folder in Visual Studio Code.
2. Open `notebooks/House_Price_EDA.ipynb`.
3. Select your Python virtual environment kernel (`venv`).
4. Click **Run All** to execute all 54 cells from beginning to end.

### Option C: Re-generating All Deliverables via Command-Line Scripts
```bash
# Generate all figures and compute statistical metrics
python generate_eda_and_assets.py

# Build and execute the full Jupyter notebook programmatically
python build_and_execute_notebook.py

# Compile the publication-quality 8-page academic PDF report
python generate_pdf_report.py
```

---

## 8. The 10-Step EDA Methodology

The project adheres strictly to the 10-step methodology prescribed in the academic project brief:

### Step 1: Data Loading & Initial Exploration
- Ingests `train.csv` (1,460 rows, 81 columns).
- Computes overall missingness: exactly 19 columns contain null values.
- Identifies heavy missingness in `PoolQC` (99.52%), `MiscFeature` (96.30%), `Alley` (93.77%), `Fence` (80.75%), `MasVnrType` (59.73%), and `FireplaceQu` (47.26%).

### Step 2: Variable Classification
- Categorizes features into **Numerical Continuous** (e.g., `SalePrice`, `GrLivArea`, `TotalBsmtSF`), **Numerical Discrete** (e.g., `YearBuilt`, `YrSold`, `FullBath`), **Categorical Nominal** (e.g., `Neighborhood`, `HouseStyle`, `SaleCondition`), and **Ordinal** (e.g., `OverallQual`, `ExterQual`, `KitchenQual`).
- Explicitly establishes ordinal mappings ($Po < Fa < TA < Gd < Ex$) and documents that `OverallQual` is stored as an integer (1–10) but is fundamentally an ordinal metric.

### Step 3: Descriptive Statistics
Computes full parametric and non-parametric metrics:
- **`SalePrice`:** Mean = **$180,921.20**, Median = **$163,000.00**, Mode = **$140,000.00**, Standard Deviation = **$79,442.50**, IQR = **$84,025.00**, Skewness = **+1.883**, Kurtosis = **6.536**.
- **`GrLivArea`:** Mean = **1,515.46 sq ft**, Median = **1,464.00 sq ft**, IQR = **647.25 sq ft**, Skewness = **+1.367**.
- **`LotArea`:** Mean = **10,516.83 sq ft**, Median = **9,478.50 sq ft**, IQR = **4,048.00 sq ft**, Skewness = **+12.208**.
- **Categorical Centers:** `Neighborhood` mode is **NAmes** (225 properties); `HouseStyle` mode is **1Story** (726 properties).

### Step 4: Distribution Analysis
- Generates raw `SalePrice` histogram with KDE overlay, boxplot, and log-transformed histogram.
- Demonstrates that $\ln(\text{SalePrice} + 1)$ reduces skewness from **+1.883** down to **+0.121**, stabilizing variance into a near-perfect Gaussian distribution.
- Illustrates upward price progression across `OverallQual` ratings and `Neighborhood` zones.

### Step 5: Correlation and Covariance Analysis
- Computes sample covariance and Pearson correlation ($r$) matrices.
- Demonstrates that Pearson correlation is scale-invariant, whereas covariance depends on arbitrary physical measurement units.
- Identifies the top numerical predictors of `SalePrice`:
  1. `OverallQual` ($r = 0.791$, $r^2 = 62.6\%$)
  2. `GrLivArea` ($r = 0.709$, $r^2 = 50.2\%$)
  3. `GarageCars` ($r = 0.640$, $r^2 = 41.0\%$)
  4. `GarageArea` ($r = 0.623$, $r^2 = 38.9\%$)
  5. `TotalBsmtSF` ($r = 0.614$, $r^2 = 37.6\%$)
  6. `1stFlrSF` ($r = 0.606$, $r^2 = 36.7\%$)
- Explains why correlation does not imply causation (e.g., adding garage bays does not mechanically inflate home price; garage size proxies overall luxury and lot dimensions).

### Step 6: Scatter Plots and Pair Plots
- Evaluates bivariate co-movement for `GrLivArea`, `TotalBsmtSF`, and `YearBuilt` against `SalePrice`.
- Annotates severe atypical properties (`Id 524` and `Id 1299`) that possess massive floor plans (>4,600 sq ft) but sold below $200,000.
- Constructs a 5-variable multivariate Seaborn pair plot with diagonal KDEs.

### Step 7: Correlation Heatmap
- Builds a Seaborn heatmap for the top 10 features using a diverging `coolwarm` palette centered at 0.0.
- Applies an upper-triangular boolean mask to eliminate visual redundancy.

### Step 8: Outlier Detection
Implements and contrasts dual detection frameworks:
- **Tukey's IQR Method ($[Q_1 - 1.5\text{IQR}, Q_3 + 1.5\text{IQR}]$):** Flags **61 outliers** in `SalePrice` ($>\$340,037.50$) and **31 outliers** in `GrLivArea` ($>2,747.62\text{ sq ft}$).
- **Parametric $Z$-Score Rule ($|z| > 3.0$):** Flags **22 outliers** in `SalePrice` and **16 outliers** in `GrLivArea`.
- **Methodological Overlap:** 100% of $Z$-score outliers are a strict subset of the IQR outliers.
- **Outlier Decision:** Retains valid luxury properties; documents and flags abnormal transfer anomalies (`Id 524`, `Id 1299`).

### Step 9: Data Quality Checks and Cleaning
- Confirms **0 duplicate rows** and 0 categorical casing/whitespace inconsistencies.
- Replaces pseudo-missing values with `'None'` in 15 structural amenity features (`PoolQC`, `MiscFeature`, `Alley`, `Fence`, `FireplaceQu`, etc.).
- Imputes missing `LotFrontage` using the **median of the corresponding Neighborhood**, respecting municipal zoning standards.
- Validates logical boundaries: 0 construction date violations (`YearBuilt <= YrSold`), 0 negative area measurements, and 0 non-positive prices.
- Generates an authoritative, 0-missing cleaned dataset: `outputs/cleaned_dataset.csv`.

### Step 10: Final 2×2 EDA Dashboard
Consolidates macro-level findings into `outputs/eda_dashboard.png`:
- **Panel 1 (Line Plot):** Longitudinal mean price by `YearBuilt` with 10-year rolling average.
- **Panel 2 (Horizontal Bar Chart):** Top 10 Ames neighborhoods by mean price.
- **Panel 3 (Density Plot):** Target `SalePrice` histogram with KDE and mean/median markers.
- **Panel 4 (Multivariate Scatter):** `GrLivArea` vs. `SalePrice` color-mapped by `OverallQual`.

---

## 9. Key Analytical Findings & Empirical Insights

1. **Quality Over Quantity:** While physical above-ground living area (`GrLivArea`, $r = 0.709$) is a massive driver of property size, subjective material quality (`OverallQual`, $r = 0.791$) commands a higher correlation and explanatory power ($62.6\%$ vs $50.2\%$). Finish craftsmanship yields higher marginal dollar return than raw square footage.
2. **Spatial Premium Stratification:** Location within Ames induces stark valuation disparities. The three highest-priced neighborhoods (`NoRidge`, `NridgHt`, and `StoneBr`) maintain average sale prices exceeding **$310,000–$335,000**, which is more than **3.2×** the average sale price of modest subdivisions (`MeadowV` at **$98,576**).
3. **Log-Normal Target Geometry:** The raw sale price distribution exhibits pronounced right-skewness ($\gamma_1 = 1.883$) and leptokurtic peakedness ($6.536$). The mean exceeds the median by **$17,921.20**. Log transformation stabilizes the skewness down to **0.121**, satisfying linear normality requirements.
4. **Multicollinearity in Ancillary Spaces:** Modern construction exhibits structural bundling: `GarageCars` and `GarageArea` ($r = 0.882$), and `TotalBsmtSF` and `1stFlrSF` ($r = 0.820$) exhibit severe collinearity.
5. **Structural Absence vs. Data Loss:** Over 90% of null entries reflect non-existent amenities rather than dropped measurements. Treating `NA` as `'None'` preserves complete dataset cardinality (1,460 observations).

---

## 10. Academic Viva Voce & Defense Guide

When presenting this project to an academic evaluation panel or technical interviewer, be prepared to discuss these core topics:

### Q1: Why does the $Z$-score method flag fewer outliers than the IQR method on skewed data?
> **Answer:** The $Z$-score relies on the parametric sample mean ($\mu$) and standard deviation ($\sigma$). In right-skewed distributions, extreme values exert high leverage, pulling the mean upward and heavily inflating the standard deviation. A widened $\sigma$ pushes the $\mu \pm 3\sigma$ threshold outward ($\$419,249$ for `SalePrice`), allowing extreme observations to hide within the 3-sigma envelope. Conversely, Tukey's IQR relies on the 25th and 75th percentiles ($Q_1$ and $Q_3$), which are completely insensitive to tail extremes. As a result, the IQR upper bound is much tighter ($\$340,037.50$), detecting all 61 upper-tier sales.

### Q2: Why is Pearson correlation preferable to covariance for feature evaluation?
> **Answer:** Covariance ($\text{Cov}(X, Y)$) measures joint directional variability but is expressed in the product of the arbitrary measurement units of $X$ and $Y$ (e.g., $\text{sq ft}\cdot\$$ or $\text{rating}\cdot\$$). Its magnitude depends entirely on the physical scale. Pearson correlation ($r$) normalizes covariance by the product of the standard deviations ($\sigma_X \sigma_Y$), producing a scale-invariant metric bounded strictly in $[-1, +1]$.

### Q3: Why did you decide against deleting all detected outliers?
> **Answer:** Outliers in real estate often represent genuine luxury transactions rather than corrupt records. Deleting properties above $\$340,000$ would artificially truncate the market distribution, introducing severe survivorship bias. Only true data anomalies (such as `Id 524` and `Id 1299`, which were abnormal, non-arm's-length sales of massive square footage at distressed prices) should be segregated for downstream tasks.

### Q4: How did you approach missing data in columns like `PoolQC` and `GarageType`?
> **Answer:** According to the official Ames data dictionary, `NA` in these columns signifies the structural absence of that feature (i.e., the house has no pool or no garage). Replacing `NA` with `'None'` preserves the record as valid negative evidence rather than treating it as unobserved data.

---

## 11. Limitations & Future Scope

### Limitations
1. **Historical Period:** The dataset reflects transactions from 2006 to 2010 during the US Subprime Mortgage Crisis and Great Recession, which may induce macroeconomic anomalies.
2. **Geographic Localization:** Findings are specific to Ames, Iowa (a university municipality) and cannot be generalized directly to high-density coastal metropolitan markets.
3. **Absence of Macro Indicators:** Macroeconomic variables (mortgage interest rates, consumer inflation, municipal property tax levies) are not captured in the dataset.

### Future Scope
1. **Geospatial Feature Engineering:** Integrating GIS coordinate layers to calculate exact network distances to Iowa State University, transit hubs, and commercial centers.
2. **Seasonal Time-Series Decomposition:** Evaluating quarter-over-quarter transaction seasonality across cyclical spring and winter buying periods.

---

## Deliverables Verification Checklist

- [x] All 10 EDA methodology steps implemented and documented.
- [x] Jupyter Notebook (`notebooks/House_Price_EDA.ipynb`) runs cleanly without errors (22/22 code cells executed).
- [x] Markdown explanatory cells placed before every code cell and interpretation cells placed after.
- [x] All 4 primary output figures saved in `outputs/` (`eda_dashboard.png`, `correlation_heatmap.png`, `saleprice_distribution.png`, `outlier_analysis.png`).
- [x] All 6 secondary visualizations saved in `outputs/other_visualizations/`.
- [x] Authoritative cleaned dataset saved in `outputs/cleaned_dataset.csv`.
- [x] High-resolution 8-page academic PDF report compiled in `reports/EDA_Project_Report.pdf`.
- [x] Zero machine learning or predictive models implemented (100% pure EDA focus).
- [x] All statistical numbers derived directly from empirical computations on `train.csv`.
