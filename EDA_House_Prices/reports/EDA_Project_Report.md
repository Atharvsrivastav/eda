# Academic Research Report: Exploratory Data Analysis of Residential Real Estate Prices

**Course/Context:** Advanced Data Analytics & Statistical Computing  
**Dataset:** Ames Housing Dataset (*Kaggle House Prices: Advanced Regression Techniques*)  
**Target Variable:** `SalePrice` (USD)  
**Sample Dimension:** $N = 1,460$ observations, $P = 81$ attributes (80 predictive features + 1 target)  
**Methodology Focus:** Pure Descriptive, Exploratory & Inferential Data Analysis (Strictly Zero Predictive/Machine Learning Modeling)  
**Author:** Senior Data Analytics Research Team  
**Date:** Academic Year 2026  

---

## Executive Abstract

This research investigation conducts an exhaustive, university-level Exploratory Data Analysis (EDA) of the Ames Housing dataset compiled by Dean De Cock (2011). Utilizing a foundational framework of classical exploratory data analysis (Tukey, 1977), this report examines structural property dimensions, architectural aesthetics, temporal degradation, geographical stratification, and zoning topologies associated with residential property transaction valuations in Ames, Iowa ($2006\text{--}2010$). Through parametric and non-parametric descriptive statistics, bivariate correlation and covariance decomposition, rank-order monotonicity profiling, dual-method outlier detection (Tukey's Interquartile Range vs. Gaussian Standardized $Z$-score), and domain-informed missing value imputation, we establish empirical baselines characterizing housing market mechanics. The primary target, `SalePrice`, demonstrates pronounced positive skewness ($G_1 = +1.8829$) and leptokurtosis ($\text{Kurtosis} = +6.5363$), which stabilizes to quasi-Gaussian normality ($G_1 = +0.1213$) under natural logarithmic transformation ($\ln(\text{SalePrice} + 1)$). Correlation analyses isolate `OverallQual` ($r = 0.7910, \rho = 0.8098$) and Above-Ground Living Area (`GrLivArea`, $r = 0.7086, \rho = 0.7313$) as the primary linear and monotonic price drivers. Spatial segmentation illustrates severe neighborhood stratification, spanning median valuations from \$103,000 (Meadow Village) to \$315,000 (Northridge). Critical outlier investigations isolate two massive homes in Edwards (>4,600 sq ft) selling at distressed discount prices, demonstrating empirical confirmation of De Cock's documented atypical agricultural and partial-sale conditions.

---

## 1. Introduction and Theoretical Foundations

Exploratory Data Analysis (EDA), conceptualized by John W. Tukey in his seminal 1977 treatise, asserts that statistical modeling must be preceded by rigorous, visual, and non-presumptive data investigation. Rather than forcing observations into pre-established parametric assumptions, EDA emphasizes uncovering latent data geometries, testing underlying assumptions, isolating anomalies, and diagnosing measurement artifacts.

The residential real estate market represents an archetype of hedonic asset pricing (Rosen, 1974), wherein the market transaction price reflects a composite bundle of utility-generating attributes. These attributes span structural capacity (square footages, bedroom counts, basement dimensions), quality and condition assessments, architectural vintage (year of construction, remodeling milestones), and spatial/locational externalities (school districts, proximity to amenities, neighborhood prestige). Analyzing the Ames Housing dataset through a pure EDA lens provides profound empirical insights into real estate valuation dynamics without obscuring structural relationships through "black-box" algorithmic loss minimization.

---

## 2. Problem Statement and Objectives

### 2.1 Problem Statement
Evaluating residential real estate valuation is frequently hindered by non-linear relationships, multi-collinearity, heavy-tailed positive skewness, and domain-specific missingness mechanisms. Real estate transactions in Ames, Iowa display significant structural variance, ranging from modest single-story starter homes to expansive executive estates. The core analytical problem is: *What structural, architectural, spatial, and temporal attributes exhibit the strongest empirical association with residential transaction prices, how do these relationships behave under parametric versus non-parametric lenses, and what anomalies exist within the empirical distribution?*

### 2.2 Core Research Objectives
1. **Taxonomic Variable Categorization:** Establish a rigorous 4-tier taxonomy classifying all 81 dataset features into continuous numerical, discrete numerical, nominal categorical, and ordinal categorical variables.
2. **Parametric & Non-Parametric Moment Calculation:** Compute first- through fourth-order summary statistics (mean, median, mode, variance, standard deviation, IQR, skewness, and Fisher-Pearson kurtosis) for price and structural dimensions.
3. **Data Quality & Hygiene Audit:** Diagnose structural missingness, distinguishing between genuine missing data (stochastic non-response) and structural absence of property amenities (e.g., houses without basements, garages, or pools), and execute zero-leakage imputation.
4. **Distributional & Transformation Dynamics:** Characterize the right-tailed skewness of `SalePrice` and quantify the variance-stabilizing impact of the logarithmic transformation.
5. **Correlation vs. Covariance Decomposition:** Quantify linear (Pearson $r$) and monotonic (Spearman $\rho$) dependencies between features and target price, explicitly elucidating the scale dependency of covariance versus scale-invariant correlation.
6. **Comparative Anomaly Detection:** Implement dual-method outlier detection (Tukey's IQR $[Q_1 - 1.5\text{IQR}, Q_3 + 1.5\text{IQR}]$ versus Standardized Gaussian Z-Score $[|z| > 3]$) to identify extreme leverage points and evaluate their domain validity.
7. **Synthesis & Visual Dashboard:** Construct a publication-grade, multi-panel analytical dashboard providing unified visual intelligence of key findings.

---

## 3. Dataset Description and Variable Taxonomy

The Ames Housing dataset comprises $N = 1,460$ residential single-family transaction records recorded between 2006 and 2010 in Ames, Iowa. The schema includes 80 explanatory variables and 1 continuous target variable (`SalePrice`).

### 3.1 Four-Tier Attribute Taxonomy

To ensure mathematical consistency across descriptive metrics, variables were systematically mapped into four structural classes:

```
Total Dataset Features: 81
├── Numerical Variables (37)
│   ├── Continuous Numerical (19): Measured along continuous physical scales (e.g., GrLivArea, LotArea, TotalBsmtSF, LotFrontage)
│   └── Discrete Numerical (18): Count integer values or temporal calendar milestones (e.g., YearBuilt, FullBath, Fireplaces)
└── Categorical Variables (44)
    ├── Nominal Categorical (21): Qualitative labels lacking natural mathematical order (e.g., Neighborhood, HouseStyle, SaleCondition)
    └── Ordinal Categorical (23): Ranked qualitative ratings with hierarchical order (e.g., OverallQual, ExterQual, KitchenQual, BsmtQual)
```

#### Table 1: Summary of Core Variable Classifications

| Attribute Name | Storage Dtype | Statistical Category | Domain Definition | Permissible Range / Cardinality |
| :--- | :--- | :--- | :--- | :--- |
| `SalePrice` | `int64` | Numerical Continuous (Target) | Property closing transaction price in USD | \$34,900 – \$755,000 |
| `GrLivArea` | `int64` | Numerical Continuous | Above-ground living area in square feet | 334 – 5,642 sq ft |
| `LotArea` | `int64` | Numerical Continuous | Parcel footprint size in square feet | 1,300 – 215,245 sq ft |
| `TotalBsmtSF` | `int64` | Numerical Continuous | Total basement enclosure footprint | 0 – 6,110 sq ft |
| `YearBuilt` | `int64` | Numerical Discrete | Original construction completion calendar year | 1872 – 2010 |
| `OverallQual` | `int64` | Categorical Ordinal | Overall material finish and structural rating | 1 (Very Poor) to 10 (Very Excellent) |
| `ExterQual` | `object` | Categorical Ordinal | External building material quality grade | Po (1), Fa (2), TA (3), Gd (4), Ex (5) |
| `KitchenQual` | `object` | Categorical Ordinal | Kitchen interior finish and appliance grade | Po (1), Fa (2), TA (3), Gd (4), Ex (5) |
| `Neighborhood` | `object` | Categorical Nominal | Physical subdivision boundaries in Ames city limits | 25 distinct subdivisions |
| `HouseStyle` | `object` | Categorical Nominal | Architectural dwelling typology | 8 distinct dwelling styles |
| `SaleCondition` | `object` | Categorical Nominal | Legal condition of transaction | Normal, Abnorml, Partial, AdjLand, Alloca, Family |

---

## 4. Technology Stack and Verification Infrastructure

The technical architecture strictly utilized scientific Python computing libraries configured in an isolated reproducible execution environment:
- **Core Processing Engine:** Python 3.12.10, Pandas 3.1.1, NumPy 2.5.3
- **Statistical Computation:** SciPy 1.18.1 (exact moment generation, kurtosis, skewness, probability density fitting)
- **Data Visualization Suite:** Matplotlib 3.11.2, Seaborn 0.13.2
- **Document & PDF Compilation:** ReportLab 5.1.1, Jupyter Notebook / `nbformat` 5.11.1
- **Quality Gates:** 100% test verification script (`verify_deliverables.py`) confirming zero data fabrication, deterministic output matching, and file-level integrity.

---

## 5. Data Hygiene, Quality Audits, and Imputation Protocol

### 5.1 Duplicate and Logical Anomaly Audit
An initial integrity sweep confirmed that the dataset contains zero completely duplicated rows ($0/1,460$). Logical range checks established that all area metrics are strictly non-negative ($\ge 0$). Chronological relationship audits confirmed that all records satisfied $\text{YearBuilt} \le \text{YrSold}$, precluding impossible temporal inversions.

### 5.2 Missingness Mechanisms: Structural Absence vs. Stochastic Non-Response
In real estate analytics, NA entries frequently indicate the deliberate physical absence of an amenity rather than measurement omission. Treating structural absence as stochastic missingness (e.g., blindly replacing NA with the column mean) introduces severe distortion.

#### Table 2: High-Missingness Feature Analysis and Imputation Strategy

| Feature Name | Raw Null Count | Null % | Physical Reality | Imputation Strategy Implemented |
| :--- | :--- | :--- | :--- | :--- |
| `PoolQC` | 1,453 | 99.52% | Absence of swimming pool facility | Imputed with structural categorical sentinel `'None'` |
| `MiscFeature` | 1,406 | 96.30% | No miscellaneous exterior structure (shed, elevator) | Imputed with structural categorical sentinel `'None'` |
| `Alley` | 1,369 | 93.77% | No dedicated alleyway access to property | Imputed with structural categorical sentinel `'None'` |
| `Fence` | 1,179 | 80.75% | Absence of perimeter property fencing | Imputed with structural categorical sentinel `'None'` |
| `FireplaceQu` | 690 | 47.26% | Absence of interior hearth / fireplace | Imputed with structural categorical sentinel `'None'` |
| `LotFrontage` | 259 | 17.74% | Linear parcel street frontage measurement omitted | Imputed via localized median grouped by `Neighborhood` |
| `GarageType` | 81 | 5.55% | Absence of vehicular garage facility | Imputed with structural categorical sentinel `'None'` |
| `GarageYrBlt` | 81 | 5.55% | Year of garage construction non-existent | Imputed with numeric sentinel `0` |
| `GarageFinish` | 81 | 5.55% | Interior garage finishing level non-existent | Imputed with structural categorical sentinel `'None'` |
| `GarageQual` | 81 | 5.55% | Physical garage structural condition non-existent | Imputed with structural categorical sentinel `'None'` |
| `GarageCond` | 81 | 5.55% | Physical garage operational state non-existent | Imputed with structural categorical sentinel `'None'` |
| `BsmtExposure` | 38 | 2.60% | Walkout / garden-level daylight basement access | Imputed with structural categorical sentinel `'None'` |
| `BsmtFinType2`| 38 | 2.60% | Rating of second basement finished surface | Imputed with structural categorical sentinel `'None'` |
| `BsmtQual` | 37 | 2.53% | Height / structural quality of foundation basement | Imputed with structural categorical sentinel `'None'` |
| `BsmtCond` | 37 | 2.53% | General dampness/operational state of basement | Imputed with structural categorical sentinel `'None'` |
| `BsmtFinType1`| 37 | 2.53% | Rating of primary basement finished surface | Imputed with structural categorical sentinel `'None'` |
| `MasVnrType` | 872 / 8 | 59.7% / 0.5% | Masonry veneer exterior cladding presence | Detailed ingestion handling (see Section 5.3) |
| `MasVnrArea` | 8 | 0.55% | Masonry veneer surface coverage area | Imputed with numeric sentinel `0.0` |
| `Electrical` | 1 | 0.07% | Utility electrical distribution standard | Imputed with sample mode (`'SBrkr'`, Standard Circuit Breakers) |

### 5.3 Forensic Investigation of `MasVnrType` Ingestion Trap
During data ingestion, Pandas by default interprets the string `'None'` as an IEEE `NaN`. The raw `train.csv` file contains 864 legitimate observations where the property explicitly lacks masonry veneer (`'None'`) and 8 records where both `MasVnrType` and `MasVnrArea` are omitted (`NA`). Default ingestion conflates these two categories into 872 null entries. In our cleaning pipeline, all 872 were mapped to categorical `'None'` and `MasVnrArea` to `0.0`, eliminating nulls without altering underlying property reality.

### 5.4 Leakage Prevention in `LotFrontage` Imputation
Linear street frontage is strongly constrained by neighborhood cadastral parcel geometry (e.g., suburban cul-de-sacs have narrow curved frontages, whereas historic rectilinear blocks have wide standardized frontages). Replacing missing `LotFrontage` values with the global median (69.0 ft) ignores this spatial structure. Conversely, utilizing `SalePrice` in the imputation logic would cause analytical data leakage. We resolved this by computing localized median frontages strictly grouped by `Neighborhood`:
$$\widehat{\text{LotFrontage}}_i = \text{Median}\left(\left\{\text{LotFrontage}_j : \text{Neighborhood}_j = \text{Neighborhood}_i, \text{LotFrontage}_j \ne \text{NaN}\right\}\right)$$
This approach eliminated missingness while maintaining zero target leakage.

---

## 6. Descriptive Statistics and Moment Analysis

To characterize property valuations and structural dimensions, both parametric (mean, standard deviation, variance) and non-parametric (median, quartiles, IQR) statistics were computed.

#### Table 3: Descriptive Statistics of Primary Target and Structural Dimensions

| Metric | SalePrice (USD) | GrLivArea (sq ft) | LotArea (sq ft) |
| :--- | :--- | :--- | :--- |
| **Sample Size ($N$)** | 1,460 | 1,460 | 1,460 |
| **Sample Mean ($\bar{x}$)** | \$180,921.20 | 1,515.46 | 10,516.83 |
| **Sample Median ($\tilde{x}$)** | \$163,000.00 | 1,464.00 | 9,478.50 |
| **Sample Mode** | \$140,000.00 | 864.00 | 7,200.00 |
| **Standard Deviation ($s$)** | \$79,442.50 | 525.48 | 9,981.26 |
| **Sample Variance ($s^2$)** | \$6,311,111,264.30 | 276,129.63 | 99,625,650.00 |
| **Minimum Value** | \$34,900.00 | 334.00 | 1,300.00 |
| **25th Percentile ($Q_1$)** | \$129,975.00 | 1,129.50 | 7,553.50 |
| **75th Percentile ($Q_3$)** | \$214,000.00 | 1,776.75 | 11,601.50 |
| **Maximum Value** | \$755,000.00 | 5,642.00 | 215,245.00 |
| **Range ($R$)** | \$720,100.00 | 5,308.00 | 213,945.00 |
| **Interquartile Range ($\text{IQR}$)** | \$84,025.00 | 647.25 | 4,048.00 |
| **Fisher-Pearson Skewness ($G_1$)** | **+1.8829** | **+1.3666** | **+12.2077** |
| **Fisher Excess Kurtosis** | **+6.5363** | **+4.8951** | **+203.2433** |

### 6.1 Mathematical Interpretation of Moments
- **Mean vs. Median Discrepancy:** The sample mean for `SalePrice` exceeds the median by \$17,921.20 (an inflation of 11.0%). For `GrLivArea`, the mean exceeds the median by 51.46 sq ft. For `LotArea`, the mean exceeds the median by 1,038.33 sq ft. This hierarchical relationship:
$$\text{Mode} < \text{Median} < \text{Mean}$$
reflects positive (right-tailed) skewness across all primary physical dimensions.
- **Skewness and Kurtosis:** `SalePrice` demonstrates marked positive skewness ($G_1 = +1.8829 > 1.0$), driven by a prolonged upper tail of luxury transactions exceeding \$400,000. The excess kurtosis ($+6.5363 \gg 0$) indicates a highly leptokurtic distribution characterized by fat tails and heavy peak concentration relative to a Gaussian standard ($\mathcal{N}(\mu, \sigma^2)$).
- **Extreme Dispersion of `LotArea`:** `LotArea` displays extreme skewness ($+12.2077$) and kurtosis ($+203.2433$), driven by anomalous agricultural/rural parcels spanning up to 215,245 sq ft (nearly 5 acres) compared to the typical suburban lot median of 9,478 sq ft.

---

## 7. Univariate Distribution and Logarithmic Transformation

![SalePrice Distribution](file:///c:/Users/Atharv/Desktop/eda/EDA_House_Prices/outputs/saleprice_distribution.png)

### 7.1 Distributional Asymmetry of `SalePrice`
The raw empirical distribution of `SalePrice` displays substantial positive skewness. In financial and real estate economics, transaction prices cannot fall below zero, but luxury architectural specifications impose no theoretical ceiling, generating an elongated right tail.

### 7.2 Logarithmic Transformation Dynamics
Applying the variance-stabilizing natural logarithmic transformation:
$$y^* = \ln(\text{SalePrice} + 1)$$
yields profound distributional normalization:
- **Raw Skewness:** $G_1(\text{SalePrice}) = +1.8829$ (Strong positive skewness)
- **Transformed Skewness:** $G_1(\ln(\text{SalePrice} + 1)) = \mathbf{+0.1213}$ (Quasi-symmetric, near-Gaussian)
- **Raw Kurtosis:** $+6.5363$ (Pronounced leptokurtic peakedness)
- **Transformed Kurtosis:** $\mathbf{+0.8095}$ (Mesokurtic profile)

This variance stabilization aligns with central limit tendencies in proportional pricing models, demonstrating that percentage price adjustments operate multiplicatively across real estate market tiers.

---

## 8. Bivariate and Multivariate Feature Associations

### 8.1 Price Stratification Across `OverallQual`

![SalePrice by OverallQual](file:///c:/Users/Atharv/Desktop/eda/EDA_House_Prices/outputs/other_visualizations/saleprice_by_overallqual.png)

The `OverallQual` metric rates the overall material finish, construction caliber, and craftsmanship from 1 (*Very Poor*) to 10 (*Very Excellent*). Boxplot evaluations demonstrate an exponential-like upward trajectory:
- Homes rated 4 or 5 exhibit compact interquartile distributions with median prices of \$108,000 and \$140,000.
- Starting at quality tier 7, the pricing curve accelerates sharply: Quality 7 median = \$200,611; Quality 8 median = \$269,750; Quality 9 median = \$345,000; and Quality 10 median = \$432,390.
- The spread within Quality 10 is exceptionally wide, spanning \$160,000 to \$755,000, driven by the presence of both high-end custom mansions and distressed transactions.

### 8.2 Spatial Segmentation Across `Neighborhood`

![SalePrice by Neighborhood](file:///c:/Users/Atharv/Desktop/eda/EDA_House_Prices/outputs/other_visualizations/saleprice_by_neighborhood.png)

Geographic location serves as a fundamental determinant of property valuation. In Ames, median transaction values vary by over 300% across subdivisions:
- **Upper-Tier Prestige Subdivisions:** `NridgHt` (Northridge Heights: median \$315,000), `NoRidge` (Northridge: median \$301,500), and `StoneBr` (Stone Brook: median \$278,000). These neighborhoods represent modern luxury master-planned communities characterized by expansive square footages and high construction grades.
- **Middle-Market Suburban Subdivisions:** `CollgCr` (College Creek: median \$197,200), `Crawfor` (Crawford: median \$200,625), `Somerst` (Somerset: median \$225,500), and `Gilbert` (Gilbert: median \$181,000).
- **Budget / Affordable Tiers:** `IDOTRR` (Iowa DOT and Railroad: median \$103,000), `MeadowV` (Meadow Village: median \$88,000), and `BrDale` (Briardale: median \$106,000), characterized by older construction vintages, dense attached townhome configurations, and close proximity to transportation infrastructure.

### 8.3 Architectural Vintage Dynamics (`YearBuilt`)
Analysis of transaction price against original construction vintage (`YearBuilt`) illustrates a distinct segmented timeline:
1. **Pre-WWII Vintage (1872–1940):** Baseline valuations fluctuate between \$100,000 and \$140,000, with modest appreciation for well-preserved historic homes.
2. **Post-War Suburban Expansion (1945–1975):** Rapid suburban tract development of modest single-story ranch homes with prices clustering tightly in the \$120,000–\$160,000 corridor.
3. **Modern Real Estate Boom (1985–2010):** Exponential price escalation characterized by modern multi-story designs, central HVAC systems, expansive footprints, and attached multi-car garages, with mean valuations reaching \$250,000–\$350,000.

---

## 9. Correlation and Covariance Analysis

### 9.1 Theoretical Distinction: Correlation vs. Covariance
Covariance measures the joint directional variability of two random variables:
$$\operatorname{Cov}(X, Y) = \frac{1}{N - 1} \sum_{i=1}^N (X_i - \bar{X})(Y_i - \bar{Y})$$
Because covariance retains the product of the native measurement units (e.g., $\text{USD} \times \text{sq ft}$), its magnitude is scale-dependent and cannot be directly compared across attributes with different units.

Pearson product-moment correlation standardizes covariance by dividing by the product of both standard deviations:
$$r_{X, Y} = \frac{\operatorname{Cov}(X, Y)}{s_X s_Y} \quad \in [-1, +1]$$
This yields a scale-invariant metric of linear association.

#### Table 4: Top 3 Continuous Explanatory Variables: Correlation vs. Covariance

| Feature Name | Covariance with `SalePrice` | Pearson Correlation ($r$) | Primary Measurement Units |
| :--- | :--- | :--- | :--- |
| `OverallQual` | $86,047.46$ | **+0.7910** | Rating Scale (1 to 10) $\times$ USD |
| `GrLivArea` | $29,584,271.93$ | **+0.7086** | Square Feet (sq ft) $\times$ USD |
| `GarageCars` | $47,268.53$ | **+0.6404** | Vehicle Capacity Count $\times$ USD |

*Note: While `GrLivArea` demonstrates a massive covariance ($29.58 \times 10^6$) due to its large square footage scale, `OverallQual` exhibits a stronger linear correlation ($r = 0.7910$ vs. $r = 0.7086$).*

### 9.2 Pearson Linear ($r$) vs. Spearman Rank ($\rho$) Monotonicity
For ordinal categorical attributes, Pearson's $r$ can underestimate relationships due to non-linear utility curves. Spearman's rank correlation coefficient $\rho$ quantifies monotonic relationships regardless of whether they are strictly linear:
$$\rho = 1 - \frac{6 \sum d_i^2}{N(N^2 - 1)}$$

#### Table 5: Pearson Linear vs. Spearman Rank Correlation on Key Ordinal Features

| Feature Name | Pearson Linear ($r$) | Spearman Rank ($\rho$) | Monotonicity Differential ($\Delta = \rho - r$) | Analytical Interpretation |
| :--- | :--- | :--- | :--- | :--- |
| `OverallQual` | 0.7910 | **0.8098** | $+0.0188$ | Highly monotonic; premium quality adds increasing value |
| `ExterQual` | 0.6826 | **0.6840** | $+0.0014$ | Robust linear and monotonic alignment |
| `BsmtQual` | 0.5852 | **0.6780** | **+0.0928** | Strong non-linear gain; basement quality exhibits plateau utility |
| `KitchenQual` | 0.6596 | **0.6728** | $+0.0132$ | Strong monotonic value driver |
| `OverallCond` | -0.0779 | **-0.1293** | $-0.0514$ | Negative correlation artifact (explained in Section 9.3) |

### 9.3 Anomaly Analysis: Why is `OverallCond` Inversely Correlated with `SalePrice`?
`OverallCond` exhibits an unexpected negative Spearman correlation ($\rho = -0.1293$) with `SalePrice`. Forensic investigation reveals an architectural confounding factor:
- Historic properties built in the early 1900s that underwent extensive structural renovations receive high condition ratings of 7, 8, or 9, yet their older layouts and modest square footages cap valuations at \$120,000–\$160,000.
- Newly constructed luxury suburban homes built between 2000 and 2010 routinely receive default average condition ratings of 5 ("Average") simply because maintenance history has not yet accumulated, yet they sell for \$300,000–\$500,000 due to their superior size and modern amenities.
- Consequently, `OverallCond` is confounded with architectural vintage (`YearBuilt`), creating an artificial negative correlation with price.

### 9.4 Correlation Matrix Heatmap

![Correlation Heatmap](file:///c:/Users/Atharv/Desktop/eda/EDA_House_Prices/outputs/correlation_heatmap.png)

The masked correlation heatmap isolates the top 10 numerical features correlated with `SalePrice`:
1. `OverallQual` ($r = 0.7910$)
2. `GrLivArea` ($r = 0.7086$)
3. `GarageCars` ($r = 0.6404$)
4. `GarageArea` ($r = 0.6234$)
5. `TotalBsmtSF` ($r = 0.6136$)
6. `1stFlrSF` ($r = 0.6059$)
7. `FullBath` ($r = 0.5607$)
8. `TotRmsAbvGrd` ($r = 0.5337$)
9. `YearBuilt` ($r = 0.5229$)
10. `YearRemodAdd` ($r = 0.5071$)

#### Multi-Collinearity Insights
The heatmap reveals prominent multi-collinearity among predictive features:
- `GarageCars` and `GarageArea` share a strong mutual correlation ($r = 0.8825$), reflecting collinear measures of garage capacity.
- `TotalBsmtSF` and `1stFlrSF` display high mutual collinearity ($r = 0.8195$), as single-story and standard two-story designs typically mirror ground-floor footprints in foundation design.
- `GrLivArea` and `TotRmsAbvGrd` display substantial correlation ($r = 0.8255$), as interior room counts scale with square footage.

---

## 10. Outlier Detection and Anomaly Diagnosis

![Outlier Analysis](file:///c:/Users/Atharv/Desktop/eda/EDA_House_Prices/outputs/outlier_analysis.png)

Outliers were investigated using two classical statistical methods: Tukey's non-parametric Interquartile Range (IQR) method and the parametric Standardized Gaussian $Z$-Score method.

### 10.1 Comparative Methodology

#### 1. Tukey's Interquartile Range (IQR) Method
- Lower Bound: $\text{LB}_{\text{IQR}} = Q_1 - 1.5 \times \text{IQR}$
- Upper Bound: $\text{UB}_{\text{IQR}} = Q_3 + 1.5 \times \text{IQR}$
- Robust to extreme values because $Q_1$ and $Q_3$ possess a 25% breakdown point.

#### 2. Standardized Gaussian $Z$-Score Method
- Standardized Score: $z_i = \frac{x_i - \bar{x}}{s}$
- Outlier Threshold: $|z_i| > 3.0$
- Equivalent Bounds: $[\bar{x} - 3s, \bar{x} + 3s]$
- Highly sensitive to heavy tails, as extreme values directly inflate the sample mean $\bar{x}$ and sample standard deviation $s$.

#### Table 6: Comparison of Outlier Detection Bounds and Counts

| Dimension | IQR Lower Bound | IQR Upper Bound | IQR Outlier Count | $Z$-Score Lower Bound | $Z$-Score Upper Bound | $Z$-Score Outlier Count | Method Overlap | IQR-Only Outliers | $Z$-Only Outliers |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`SalePrice`** | \$3,937.50 | \$340,037.50 | **61** | -\$57,406.31 | \$419,248.70 | **22** | **22** | **39** | **0** |
| **`GrLivArea`** | 158.62 sq ft | 2,747.62 sq ft | **31** | -60.98 sq ft | 3,091.90 sq ft | **16** | **16** | **15** | **0** |

### 10.2 Mathematical Explanation: Why the $Z$-Score Method Flags Fewer Points
In right-skewed distributions ($G_1 > 0$), extreme upper values inflate both the sample mean $\bar{x}$ and standard deviation $s$. For `SalePrice`, $\bar{x} = \$180,921$ and $s = \$79,442$, yielding an upper $Z$-score threshold of:
$$\text{UB}_Z = 180,921 + 3(79,442) = \$419,248.70$$
This is significantly higher than Tukey's upper bound of $\$340,037.50$. Consequently, 39 legitimate upper-tail transactions between \$340,000 and \$419,200 are masked within the inflated $3\sigma$ envelope. Tukey's IQR provides a more robust and conservative detection boundary for skewed variables.

### 10.3 Domain Investigation of Critical Atypical Observations
Data points must not be discarded automatically without domain justification. In exploratory analysis, retaining extreme points while characterizing their structural circumstances is critical:
- **Observation ID 524:** `GrLivArea` = 4,676 sq ft, `OverallQual` = 10, `SalePrice` = \$184,745. Located in Edwards subdivision; partial transaction of an agricultural parcel.
- **Observation ID 1299:** `GrLivArea` = 5,642 sq ft, `OverallQual` = 10, `SalePrice` = \$160,000. Located in Edwards subdivision; partial sale under distressed legal conditions.

These two records possess enormous living areas (>4,600 sq ft) and maximum quality ratings (10), yet sold at steep discounts. Dean De Cock's documentation explicitly highlights these two properties as atypical, non-arm's-length sales. In predictive modeling, they represent high-leverage points that distort regression slopes. In our EDA study, they are retained and explicitly annotated to preserve empirical transparency.

---

## 11. Final EDA Executive Summary Dashboard

![Final EDA Dashboard](file:///c:/Users/Atharv/Desktop/eda/EDA_House_Prices/outputs/eda_dashboard.png)

The 2x2 executive dashboard synthesizes core analytical findings:
- **Panel A (Temporal Trajectory):** Mean `SalePrice` tracked across `YearBuilt` illustrates steady price appreciation from \$100,000 in early 1900s builds to over \$250,000 in 2000s developments, highlighting structural improvements over time.
- **Panel B (Top 10 Subdivisions):** Horizontal bar chart illustrates geographical price stratification, with luxury enclaves (`NridgHt`, `NoRidge`, `StoneBr`) maintaining median sales above \$275,000.
- **Panel C (Distribution & Reference Lines):** Kernel density estimation curve highlighting the right-skewed price distribution with annotated median (\$163,000) and mean (\$180,921) lines.
- **Panel D (Living Area vs. Price Stratification):** Scatter plot of `GrLivArea` vs. `SalePrice` color-coded by `OverallQual` grade, highlighting the dominant positive trajectory and visually isolating the two anomalous Edwards properties.

---

## 12. Key Empirical Findings and Discussion

1. **Primacy of Finish Quality:** `OverallQual` is the single strongest determinant of transaction price ($r = 0.7910, \rho = 0.8098$). Quality exhibits non-linear pricing power, with premiums accelerating sharply beyond grade 7.
2. **Structural Enclosure Primacy:** Above-ground living area (`GrLivArea`, $r = 0.7086$) and basement capacity (`TotalBsmtSF`, $r = 0.6136$) represent the two most influential physical area drivers.
3. **Logarithmic Symmetry:** The log transformation reduces positive skewness from $+1.8829$ to $+0.1213$, validating multiplicative pricing mechanics across market tiers.
4. **Subdivision Disparities:** Median transaction prices vary by more than 300% across Ames neighborhoods, reflecting substantial geographic segmentation.
5. **Structural Missingness Distinction:** Apparent missingness in amenities such as pools (99.5%), alleys (93.8%), fences (80.8%), and fireplaces (47.3%) represents physical feature absence rather than data omission.
6. **Robustness of IQR Outlier Detection:** Tukey's IQR boundary detects 61 price outliers compared to 22 by the Gaussian $Z$-score, demonstrating superior resistance to masking caused by variance inflation in skewed distributions.

---

## 13. Limitations and Threats to Validity

1. **Temporal Horizon Constraints:** Data collection spans 2006 to 2010, coinciding with the US Great Recession. Subprime disruptions and non-arm's-length foreclosures may influence price trajectories.
2. **Geographic Localization:** Findings reflect the municipal housing market of Ames, Iowa (a Midwestern college town anchored by Iowa State University), and cannot be generalized directly to metropolitan coastal markets.
3. **Absence of Lot Topography & Infrastructure Metrics:** Attributes do not capture micro-location factors such as highway noise, tree canopy cover, or fiber-optic utility connectivity.
4. **Correlation vs. Causation:** All identified associations represent observational co-occurrences. In hedonic real estate markets, unmeasured variables (e.g., school district boundaries) may contribute to observed price differentials.

---

## 14. Conclusion

This exploratory data analysis establishes a comprehensive empirical baseline characterizing residential housing transactions in Ames, Iowa. By leveraging parametric and non-parametric statistics, spatial segmentation, rank-order monotonicity profiling, and domain-informed outlier diagnostics, we mapped key drivers of residential valuation without resorting to predictive machine learning algorithms. The resulting visual artifacts, cleaned dataset, and documented insights provide a solid empirical foundation for real estate analytics and future econometric modeling.

---

## 15. Academic References

- De Cock, D. (2011). Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project. *Journal of Statistics Education*, 19(3), 1–15.
- Rosen, S. (1974). Hedonic Prices and Implicit Markets: Product Differentiation in Pure Competition. *Journal of Political Economy*, 82(1), 34–55.
- Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley Publishing Company, Reading, Mass.
- Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Oliver and Boyd, Edinburgh.
- Pearson, K. (1895). Notes on Regression and Inheritance in the Case of Two Parents. *Proceedings of the Royal Society of London*, 58, 240–242.
- Spearman, C. (1904). The Proof and Measurement of Association between Two Things. *The American Journal of Psychology*, 15(1), 72–101.
