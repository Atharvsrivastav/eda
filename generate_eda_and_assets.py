import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import Patch
import seaborn as sns
from scipy import stats

# ==============================================================================
# GLOBAL AESTHETICS & THEME SETUP
# ==============================================================================
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['axes.edgecolor'] = '#CBD5E0'
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.labelweight'] = 'semibold'
plt.rcParams['xtick.labelsize'] = 9.5
plt.rcParams['ytick.labelsize'] = 9.5
plt.rcParams['grid.color'] = '#E2E8F0'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.7

# Palette definition
NAVY_PRIMARY = '#1A365D'
BLUE_SECONDARY = '#2B6CB0'
BLUE_LIGHT = '#EBF8FF'
TEAL_ACCENT = '#319795'
CORAL_ACCENT = '#DD6B20'
CRIMSON_ALERT = '#E53E3E'
GREEN_SUCCESS = '#2F855A'
GRAY_TEXT = '#2D3748'
GRAY_MUTED = '#718096'
GRAY_BG = '#F7FAFC'

outputs_dir = 'EDA_House_Prices/outputs'
other_viz_dir = 'EDA_House_Prices/outputs/other_visualizations'
os.makedirs(outputs_dir, exist_ok=True)
os.makedirs(other_viz_dir, exist_ok=True)

# Helper currency formatter
def currency_fmt(x, pos):
    if x >= 1e6:
        return f"${x*1e-6:.1f}M"
    elif x >= 1e3:
        return f"${x*1e-3:.0f}k"
    else:
        return f"${x:.0f}"

curr_formatter = ticker.FuncFormatter(currency_fmt)
comma_formatter = ticker.FuncFormatter(lambda x, p: f"{int(x):,}")

# Load data
data_path = 'EDA_House_Prices/data/train.csv'
df = pd.read_csv(data_path)
print(f"Loaded dataset: {df.shape}")

# Categorical and numerical columns
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(include=['object', 'string']).columns.tolist()

# Compute core descriptive stats
stats_vars = ['SalePrice', 'GrLivArea', 'LotArea']
desc_stats = {}
for col in stats_vars:
    series = df[col].dropna()
    desc_stats[col] = {
        'Mean': float(series.mean()),
        'Median': float(series.median()),
        'Mode': float(series.mode().iloc[0]),
        'Std': float(series.std()),
        'Variance': float(series.var()),
        'Min': float(series.min()),
        'Max': float(series.max()),
        'Range': float(series.max() - series.min()),
        'Q1': float(series.quantile(0.25)),
        'Q3': float(series.quantile(0.75)),
        'IQR': float(series.quantile(0.75) - series.quantile(0.25)),
        'Skewness': float(series.skew()),
        'Kurtosis': float(series.kurtosis()),
        'Skew_Direction': 'Right-skewed (Mean > Median)' if series.mean() > series.median() else 'Left-skewed'
    }

# ==============================================================================
# 1. UPGRADED: SALEPRICE DISTRIBUTION (saleprice_distribution.png)
# ==============================================================================
print("Generating upgraded saleprice_distribution.png...")
fig, axes = plt.subplots(1, 3, figsize=(19, 5.8))
fig.patch.set_facecolor('white')

# Panel A: Raw SalePrice Hist + KDE
ax0 = axes[0]
ax0.set_facecolor('white')
sns.histplot(df['SalePrice'], kde=True, ax=ax0, color=NAVY_PRIMARY, bins=35, edgecolor='#0F2942', alpha=0.55,
             line_kws={'linewidth': 2.5, 'color': BLUE_SECONDARY})
mean_val = desc_stats['SalePrice']['Mean']
median_val = desc_stats['SalePrice']['Median']
ax0.axvline(mean_val, color=CRIMSON_ALERT, linestyle='--', linewidth=2.2, label=f"Mean: ${mean_val:,.0f}")
ax0.axvline(median_val, color=GREEN_SUCCESS, linestyle='-', linewidth=2.2, label=f"Median: ${median_val:,.0f}")
ax0.xaxis.set_major_formatter(curr_formatter)
ax0.yaxis.set_major_formatter(comma_formatter)
ax0.set_title('[A] Raw SalePrice Distribution (USD)', pad=12, color=NAVY_PRIMARY, fontsize=13)
ax0.set_xlabel('Sale Price ($ USD)', labelpad=8)
ax0.set_ylabel('Property Frequency', labelpad=8)
ax0.legend(frameon=True, facecolor=GRAY_BG, edgecolor='#CBD5E0', fontsize=9.5, loc='upper right')
# Metric callout
raw_skew = desc_stats['SalePrice']['Skewness']
raw_kurt = desc_stats['SalePrice']['Kurtosis']
ax0.text(0.53, 0.65, f"Skewness: +{raw_skew:.2f} (Right-skewed)\nExcess Kurtosis: {raw_kurt:.2f} (Leptokurtic)\nMean-Median Gap: +${mean_val - median_val:,.0f}",
         transform=ax0.transAxes, fontsize=8.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#FEFCBF', edgecolor='#ECC94B', alpha=0.9))
sns.despine(ax=ax0)

# Panel B: SalePrice Boxplot
ax1 = axes[1]
ax1.set_facecolor('white')
box_plot = sns.boxplot(y=df['SalePrice'], ax=ax1, color=BLUE_LIGHT, width=0.35,
                       boxprops=dict(edgecolor=NAVY_PRIMARY, linewidth=1.8),
                       whiskerprops=dict(color=NAVY_PRIMARY, linewidth=1.5),
                       capprops=dict(color=NAVY_PRIMARY, linewidth=1.5),
                       medianprops=dict(color=CRIMSON_ALERT, linewidth=2.5),
                       flierprops=dict(marker='o', markersize=4.5, markerfacecolor=CRIMSON_ALERT, markeredgecolor='none', alpha=0.6))
ax1.yaxis.set_major_formatter(curr_formatter)
ax1.set_title('[B] SalePrice Quartile Spread & Outliers', pad=12, color=NAVY_PRIMARY, fontsize=13)
ax1.set_ylabel('Sale Price ($ USD)', labelpad=8)

# Annotate Q1, Median, Q3, and Upper Bound
q1 = desc_stats['SalePrice']['Q1']
q3 = desc_stats['SalePrice']['Q3']
iqr = desc_stats['SalePrice']['IQR']
upper_bound = q3 + 1.5 * iqr
ax1.text(0.22, q1, f"Q1: ${q1:,.0f}", transform=ax1.get_yaxis_transform(), fontsize=8.5, color=GRAY_TEXT, fontweight='bold', va='center')
ax1.text(0.22, median_val, f"Median: ${median_val:,.0f}", transform=ax1.get_yaxis_transform(), fontsize=8.5, color=CRIMSON_ALERT, fontweight='bold', va='center')
ax1.text(0.22, q3, f"Q3: ${q3:,.0f}", transform=ax1.get_yaxis_transform(), fontsize=8.5, color=GRAY_TEXT, fontweight='bold', va='center')
ax1.text(0.22, upper_bound, f"Tukey Limit: ${upper_bound:,.0f}", transform=ax1.get_yaxis_transform(), fontsize=8.5, color=CORAL_ACCENT, fontweight='bold', va='center')
sns.despine(ax=ax1)

# Panel C: Log-Transformed SalePrice
ax2 = axes[2]
ax2.set_facecolor('white')
log_sp = np.log1p(df['SalePrice'])
log_skew = float(log_sp.skew())
log_kurt = float(log_sp.kurtosis())
sns.histplot(log_sp, kde=True, ax=ax2, color=TEAL_ACCENT, bins=35, edgecolor='#234E52', alpha=0.55,
             line_kws={'linewidth': 2.5, 'color': GREEN_SUCCESS})
ax2.axvline(log_sp.mean(), color=CRIMSON_ALERT, linestyle='--', linewidth=2.2, label=f"Mean: {log_sp.mean():.2f}")
ax2.axvline(log_sp.median(), color=NAVY_PRIMARY, linestyle='-', linewidth=2.2, label=f"Median: {log_sp.median():.2f}")
ax2.yaxis.set_major_formatter(comma_formatter)
ax2.set_title('[C] Log(SalePrice + 1) Density (Normalized)', pad=12, color=NAVY_PRIMARY, fontsize=13)
ax2.set_xlabel('Natural Log of Sale Price: ln(SalePrice + 1)', labelpad=8)
ax2.set_ylabel('Property Frequency', labelpad=8)
ax2.legend(frameon=True, facecolor=GRAY_BG, edgecolor='#CBD5E0', fontsize=9.5, loc='upper right')
ax2.text(0.53, 0.65, f"Skewness: +{log_skew:.3f} (Near Normal)\nExcess Kurtosis: +{log_kurt:.2f}\nNormality Restored via ln(x)",
         transform=ax2.transAxes, fontsize=8.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#C6F6D5', edgecolor='#48BB78', alpha=0.9))
sns.despine(ax=ax2)

plt.subplots_adjust(wspace=0.28)
plt.savefig(os.path.join(outputs_dir, 'saleprice_distribution.png'), dpi=300, facecolor='white')
plt.close()
print("Saved upgraded saleprice_distribution.png")

# ==============================================================================
# 2. UPGRADED: CORRELATION HEATMAP (correlation_heatmap.png)
# ==============================================================================
print("Generating upgraded correlation_heatmap.png...")
numeric_clean = df[numeric_cols].drop(columns=['Id'], errors='ignore')
corr_matrix = numeric_clean.corr(method='pearson')
top10_corr_series = corr_matrix['SalePrice'].sort_values(ascending=False).head(11)
top10_features = top10_corr_series.index.tolist()
corr_top10 = numeric_clean[top10_features].corr()

# Mask upper triangle
mask = np.triu(np.ones_like(corr_top10, dtype=bool))

fig, ax = plt.subplots(figsize=(11, 9))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Custom diverging palette: Deep Navy (-1) -> Pure White (0) -> Rich Coral/Red (+1)
cmap = sns.diverging_palette(240, 15, s=85, l=55, as_cmap=True)

heatmap = sns.heatmap(
    corr_top10, mask=mask, annot=True, fmt='.2f', cmap=cmap, center=0, vmin=-0.2, vmax=1.0,
    square=True, linewidths=1.2, linecolor='white',
    cbar_kws={
        "shrink": 0.78,
        "label": "Pearson Correlation Coefficient (r)",
        "orientation": "vertical",
        "pad": 0.03
    },
    annot_kws={"fontsize": 9.5, "fontweight": "bold", "color": GRAY_TEXT},
    ax=ax
)

ax.set_title("Pearson Correlation Heatmap: Top 10 Covariates with SalePrice\n", fontsize=15, fontweight='bold', color=NAVY_PRIMARY, loc='left')
fig.text(0.125, 0.905, "Ranked by correlation with SalePrice | Upper-triangle masked to eliminate redundant projections", fontsize=10, color=GRAY_MUTED)

ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=10, color=GRAY_TEXT, fontweight='semibold')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=10, color=GRAY_TEXT, fontweight='semibold')

plt.tight_layout()
plt.savefig(os.path.join(outputs_dir, 'correlation_heatmap.png'), dpi=300, facecolor='white')
plt.close()
print("Saved upgraded correlation_heatmap.png")

# ==============================================================================
# 3. UPGRADED: OUTLIER DETECTION (outlier_analysis.png)
# ==============================================================================
print("Generating upgraded outlier_analysis.png...")
def get_iqr_outliers(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    mask = (series < lower) | (series > upper)
    return mask, lower, upper, q1, q3, iqr

def get_zscore_outliers(series, threshold=3.0):
    mean_v = series.mean()
    std_v = series.std()
    z_scores = (series - mean_v) / std_v
    mask = np.abs(z_scores) > threshold
    return mask, z_scores, mean_v, std_v

gr_iqr_mask, gr_low, gr_up, _, _, _ = get_iqr_outliers(df['GrLivArea'])
sp_iqr_mask, sp_low, sp_up, _, _, _ = get_iqr_outliers(df['SalePrice'])
gr_z_mask, _, _, _ = get_zscore_outliers(df['GrLivArea'], 3.0)
sp_z_mask, _, _, _ = get_zscore_outliers(df['SalePrice'], 3.0)

fig, axes = plt.subplots(1, 2, figsize=(18, 6.8))
fig.patch.set_facecolor('white')

# Left Panel: GrLivArea Boxplot + Outlier Annotation
ax_l = axes[0]
ax_l.set_facecolor('white')
sns.boxplot(y=df['GrLivArea'], ax=ax_l, color=BLUE_LIGHT, width=0.35,
            boxprops=dict(edgecolor=NAVY_PRIMARY, linewidth=1.8),
            whiskerprops=dict(color=NAVY_PRIMARY, linewidth=1.5),
            capprops=dict(color=NAVY_PRIMARY, linewidth=1.5),
            medianprops=dict(color=CRIMSON_ALERT, linewidth=2.5),
            flierprops=dict(marker='o', markersize=6, markerfacecolor=CRIMSON_ALERT, markeredgecolor='black', alpha=0.7))
ax_l.set_title('[A] GrLivArea Boxplot & Tukey IQR Thresholds', pad=12, color=NAVY_PRIMARY, fontsize=13)
ax_l.set_ylabel('Above Ground Living Area (sq ft)', labelpad=8)
ax_l.yaxis.set_major_formatter(comma_formatter)
ax_l.axhline(gr_up, color=CORAL_ACCENT, linestyle='--', linewidth=1.8, label=f"Upper Bound: {gr_up:,.1f} sq ft")
ax_l.legend(frameon=True, facecolor=GRAY_BG, edgecolor='#CBD5E0', fontsize=9.5, loc='upper left')

# Annotations on boxplot
ax_l.text(0.24, desc_stats['GrLivArea']['Median'], f"Median: {desc_stats['GrLivArea']['Median']:,.0f} sq ft", 
          transform=ax_l.get_yaxis_transform(), fontsize=9, color=CRIMSON_ALERT, fontweight='bold', va='center')
ax_l.text(0.24, gr_up, f"Tukey Bound: {gr_up:,.0f} sq ft\n({gr_iqr_mask.sum()} Outliers Flagged)", 
          transform=ax_l.get_yaxis_transform(), fontsize=9, color=CORAL_ACCENT, fontweight='bold', va='center')
sns.despine(ax=ax_l)

# Right Panel: Dual-Method Outlier Scatter Plot
ax_r = axes[1]
ax_r.set_facecolor('white')

outlier_classes = np.array(['Inlier (Normal)'] * len(df), dtype=object)
outlier_classes[gr_iqr_mask | sp_iqr_mask] = 'IQR Outlier Only (n=40)'
outlier_classes[gr_z_mask | sp_z_mask] = 'Z-Score Outlier (|z|>3)'
outlier_classes[(gr_iqr_mask | sp_iqr_mask) & (gr_z_mask | sp_z_mask)] = 'Consensus Outlier (Both Methods, n=23)'

palette_dict = {
    'Inlier (Normal)': '#CBD5E0',
    'IQR Outlier Only (n=40)': '#D69E2E',
    'Z-Score Outlier (|z|>3)': '#DD6B20',
    'Consensus Outlier (Both Methods, n=23)': CRIMSON_ALERT
}

for cls_name, color in palette_dict.items():
    sub = df[outlier_classes == cls_name]
    alpha = 0.4 if cls_name == 'Inlier (Normal)' else 0.9
    size = 28 if cls_name == 'Inlier (Normal)' else 65
    edge = 'none' if cls_name == 'Inlier (Normal)' else 'black'
    ax_r.scatter(sub['GrLivArea'], sub['SalePrice'], c=color, label=cls_name, alpha=alpha, s=size, edgecolors=edge, linewidth=0.6)

# Annotate specific famous anomalies
anomalies = df[((df['GrLivArea'] > 4000) & (df['SalePrice'] < 300000)) | (df['SalePrice'] > 700000)]
for _, row in anomalies.iterrows():
    ax_r.annotate(
        f"Id {row['Id']}: {row['GrLivArea']:,} sqft, ${row['SalePrice']:,}",
        xy=(row['GrLivArea'], row['SalePrice']),
        xytext=(row['GrLivArea'] - 750, row['SalePrice'] + (45000 if row['SalePrice'] < 400000 else -40000)),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.15", color=NAVY_PRIMARY, lw=1.5),
        fontsize=8.5, fontweight='bold', color=NAVY_PRIMARY,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#EDF2F7', edgecolor='#CBD5E0', alpha=0.9)
    )

ax_r.set_title('[B] Outlier Methodology Comparison (GrLivArea vs SalePrice)', pad=12, color=NAVY_PRIMARY, fontsize=13)
ax_r.set_xlabel('Above Ground Living Area (GrLivArea sq ft)', labelpad=8)
ax_r.set_ylabel('Sale Price ($ USD)', labelpad=8)
ax_r.xaxis.set_major_formatter(comma_formatter)
ax_r.yaxis.set_major_formatter(curr_formatter)
ax_r.legend(title='Classification Status', frameon=True, facecolor=GRAY_BG, edgecolor='#CBD5E0', fontsize=9)
sns.despine(ax=ax_r)

plt.subplots_adjust(wspace=0.25)
plt.savefig(os.path.join(outputs_dir, 'outlier_analysis.png'), dpi=300, facecolor='white')
plt.close()
print("Saved upgraded outlier_analysis.png")

# ==============================================================================
# 4. UPGRADED: EXECUTIVE 2x2 EDA DASHBOARD (eda_dashboard.png)
# ==============================================================================
print("Generating upgraded eda_dashboard.png...")
fig = plt.figure(figsize=(19, 14), facecolor='white')
gs = fig.add_gridspec(2, 2, hspace=0.32, wspace=0.22, top=0.91, bottom=0.06, left=0.07, right=0.95)

# Overall Dashboard Title Banner
fig.text(0.07, 0.965, "EXECUTIVE EXPLORATORY DATA ANALYSIS DASHBOARD", fontsize=18, fontweight='heavy', color=NAVY_PRIMARY)
fig.text(0.07, 0.945, "Ames Housing Dataset (1,460 Residential Sales) | Macro-temporal, Spatial, Distributional, and Structural Drivers", fontsize=11, color=GRAY_MUTED)

# PANEL 1 (Top-Left): Historical Trend
ax_p1 = fig.add_subplot(gs[0, 0])
ax_p1.set_facecolor('white')
avg_year = df.groupby('YearBuilt')['SalePrice'].mean().reset_index()
avg_year['Rolling10'] = avg_year['SalePrice'].rolling(10, min_periods=1).mean()
ax_p1.plot(avg_year['YearBuilt'], avg_year['SalePrice'], color='#A0AEC0', linewidth=1.5, alpha=0.7, label='Annual Mean Price')
ax_p1.plot(avg_year['YearBuilt'], avg_year['Rolling10'], color=CORAL_ACCENT, linewidth=2.8, label='10-Year Rolling Mean (Trend)')
ax_p1.fill_between(avg_year['YearBuilt'], avg_year['SalePrice'], color=BLUE_LIGHT, alpha=0.5)

# Benchmark annotations
ax_p1.axvline(1950, color=GRAY_MUTED, linestyle=':', alpha=0.7)
ax_p1.text(1951, 100000, "Post-WWII Expansion", fontsize=8.5, color=GRAY_MUTED, rotation=90)
ax_p1.axvline(1985, color=GRAY_MUTED, linestyle=':', alpha=0.7)
ax_p1.text(1986, 100000, "Modern Building Codes", fontsize=8.5, color=GRAY_MUTED, rotation=90)

ax_p1.set_title("[A] Longitudinal Appreciation: Mean SalePrice by Construction Year", pad=10, fontsize=12.5, color=NAVY_PRIMARY, loc='left')
ax_p1.set_xlabel("Year Built (Original Construction)", labelpad=6)
ax_p1.set_ylabel("Average Sale Price ($ USD)", labelpad=6)
ax_p1.yaxis.set_major_formatter(curr_formatter)
ax_p1.legend(loc='upper left', frameon=True, facecolor=GRAY_BG, edgecolor='#CBD5E0', fontsize=9)
sns.despine(ax=ax_p1)

# PANEL 2 (Top-Right): Spatial Pricing Hierarchy
ax_p2 = fig.add_subplot(gs[0, 1])
ax_p2.set_facecolor('white')
top10_neigh = df.groupby('Neighborhood')['SalePrice'].mean().sort_values(ascending=False).head(10).reset_index()

# Gradient bar coloring
colors_bars = sns.color_palette("mako", n_colors=10)[::-1]
bars = ax_p2.barh(top10_neigh['Neighborhood'], top10_neigh['SalePrice'], color=colors_bars, edgecolor='none', height=0.68)
ax_p2.invert_yaxis()  # Highest on top
ax_p2.set_title("[B] Spatial Hierarchy: Top 10 Ames Neighborhoods by Mean Price", pad=10, fontsize=12.5, color=NAVY_PRIMARY, loc='left')
ax_p2.set_xlabel("Mean Sale Price ($ USD)", labelpad=6)
ax_p2.set_ylabel("Neighborhood Code", labelpad=6)
ax_p2.xaxis.set_major_formatter(curr_formatter)

# Add exact value labels inside/outside bars
for bar, val in zip(bars, top10_neigh['SalePrice']):
    ax_p2.text(val + 3500, bar.get_y() + bar.get_height()/2, f"${val:,.0f}", 
               va='center', ha='left', fontsize=8.8, fontweight='bold', color=NAVY_PRIMARY)
ax_p2.set_xlim(0, max(top10_neigh['SalePrice']) * 1.15)
sns.despine(ax=ax_p2)

# PANEL 3 (Bottom-Left): Target Distribution & Reference Lines
ax_p3 = fig.add_subplot(gs[1, 0])
ax_p3.set_facecolor('white')
sns.histplot(df['SalePrice'], kde=True, ax=ax_p3, color=NAVY_PRIMARY, bins=35, edgecolor='#0F2942', alpha=0.55,
             line_kws={'linewidth': 2.5, 'color': BLUE_SECONDARY})
ax_p3.axvline(mean_val, color=CRIMSON_ALERT, linestyle='--', linewidth=2.2, label=f"Mean: ${mean_val:,.0f}")
ax_p3.axvline(median_val, color=GREEN_SUCCESS, linestyle='-', linewidth=2.2, label=f"Median: ${median_val:,.0f}")
# Highlight IQR region
ax_p3.axvspan(q1, q3, color='#EDF2F7', alpha=0.8, label=f"IQR ($130k – $214k)")
ax_p3.xaxis.set_major_formatter(curr_formatter)
ax_p3.yaxis.set_major_formatter(comma_formatter)
ax_p3.set_title("[C] Target Density: SalePrice Asymmetry & Central Tendencies", pad=10, fontsize=12.5, color=NAVY_PRIMARY, loc='left')
ax_p3.set_xlabel("Sale Price ($ USD)", labelpad=6)
ax_p3.set_ylabel("Property Count", labelpad=6)
ax_p3.legend(loc='upper right', frameon=True, facecolor=GRAY_BG, edgecolor='#CBD5E0', fontsize=9)
sns.despine(ax=ax_p3)

# PANEL 4 (Bottom-Right): Multivariate Geometry
ax_p4 = fig.add_subplot(gs[1, 1])
ax_p4.set_facecolor('white')
sc = ax_p4.scatter(df['GrLivArea'], df['SalePrice'], c=df['OverallQual'], cmap='viridis', s=42, alpha=0.8, edgecolors='none')
cbar = fig.colorbar(sc, ax=ax_p4, orientation='vertical', pad=0.02, shrink=0.92)
cbar.set_label('Overall Quality Rating (1 = Poor, 10 = Very Excellent)', fontsize=9.5, labelpad=8)
cbar.ax.tick_params(labelsize=9)

# Regression line
sns.regplot(x='GrLivArea', y='SalePrice', data=df, ax=ax_p4, scatter=False, color=CORAL_ACCENT, line_kws={'linewidth': 2, 'linestyle': '--'})

ax_p4.set_title("[D] Multivariate Geometry: GrLivArea vs SalePrice by OverallQual", pad=10, fontsize=12.5, color=NAVY_PRIMARY, loc='left')
ax_p4.set_xlabel("Above Ground Living Area (GrLivArea sq ft)", labelpad=6)
ax_p4.set_ylabel("Sale Price ($ USD)", labelpad=6)
ax_p4.xaxis.set_major_formatter(comma_formatter)
ax_p4.yaxis.set_major_formatter(curr_formatter)
sns.despine(ax=ax_p4)

plt.savefig(os.path.join(outputs_dir, 'eda_dashboard.png'), dpi=300, facecolor='white')
plt.close()
print("Saved upgraded eda_dashboard.png")

# ==============================================================================
# 5. UPGRADED: SECONDARY VISUALIZATIONS (other_visualizations/)
# ==============================================================================
# 5A. SalePrice by OverallQual
print("Generating upgraded saleprice_by_overallqual.png...")
fig, ax = plt.subplots(figsize=(11, 6.2))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
qual_palette = sns.color_palette("crest", n_colors=10)
sns.boxplot(x='OverallQual', y='SalePrice', data=df, palette=qual_palette, hue='OverallQual', legend=False,
            boxprops=dict(linewidth=1.2), medianprops=dict(color=CRIMSON_ALERT, linewidth=2), ax=ax)

# Line connecting medians
medians = df.groupby('OverallQual')['SalePrice'].median()
ax.plot(range(len(medians)), medians.values, color=NAVY_PRIMARY, marker='o', markersize=6, linestyle='--', linewidth=2, label='Median Trend Line')

ax.set_title("SalePrice Progression Across Overall Material & Finish Quality (OverallQual)\n", fontsize=14, fontweight='bold', color=NAVY_PRIMARY, loc='left')
fig.text(0.125, 0.91, "Ratings range from 1 (Very Poor) to 10 (Very Excellent) | Red lines indicate group medians", fontsize=9.5, color=GRAY_MUTED)
ax.set_xlabel("Overall Quality Rating (1–10)", labelpad=8)
ax.set_ylabel("Sale Price ($ USD)", labelpad=8)
ax.yaxis.set_major_formatter(curr_formatter)
ax.legend(frameon=True, facecolor=GRAY_BG, edgecolor='#CBD5E0', fontsize=9.5, loc='upper left')
sns.despine(ax=ax)
plt.savefig(os.path.join(other_viz_dir, 'saleprice_by_overallqual.png'), dpi=300, facecolor='white')
plt.close()

# 5B. SalePrice by Neighborhood
print("Generating upgraded saleprice_by_neighborhood.png...")
fig, ax = plt.subplots(figsize=(15, 7.5))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
order_neigh = df.groupby('Neighborhood')['SalePrice'].median().sort_values(ascending=False).index
neigh_palette = sns.color_palette("viridis", n_colors=len(order_neigh))

sns.boxplot(x='Neighborhood', y='SalePrice', data=df, order=order_neigh, palette=neigh_palette, hue='Neighborhood', legend=False,
            boxprops=dict(linewidth=1.2), flierprops=dict(marker='o', markersize=4, alpha=0.5), ax=ax)
ax.set_title("Ames Neighborhood Price Stratification (Ranked by Median Transaction Value)\n", fontsize=14, fontweight='bold', color=NAVY_PRIMARY, loc='left')
fig.text(0.125, 0.92, "Sorted descending by median transaction price | Shows marked spatial premium disparities", fontsize=9.5, color=GRAY_MUTED)
ax.set_xlabel("Neighborhood Code", labelpad=8)
ax.set_ylabel("Sale Price ($ USD)", labelpad=8)
ax.yaxis.set_major_formatter(curr_formatter)
ax.tick_params(axis='x', rotation=45)
sns.despine(ax=ax)
plt.savefig(os.path.join(other_viz_dir, 'saleprice_by_neighborhood.png'), dpi=300, facecolor='white')
plt.close()

# 5C. Countplots of OverallQual and HouseStyle
print("Generating upgraded countplots_qual_style.png...")
fig, axes = plt.subplots(1, 2, figsize=(16, 5.5))
fig.patch.set_facecolor('white')

# OverallQual Countplot
ax_c1 = axes[0]
ax_c1.set_facecolor('white')
palette_qual = sns.color_palette("Blues_d", n_colors=10)
cp1 = sns.countplot(x='OverallQual', data=df, ax=ax_c1, palette=palette_qual, hue='OverallQual', legend=False, edgecolor='#2B6CB0')
for p in cp1.patches:
    height = p.get_height()
    pct = (height / len(df)) * 100
    ax_c1.annotate(f"{int(height)}\n({pct:.1f}%)", (p.get_x() + p.get_width() / 2., height + 6),
                   ha='center', va='bottom', fontsize=8, color=GRAY_TEXT, fontweight='bold')
ax_c1.set_ylim(0, max(df['OverallQual'].value_counts()) * 1.15)
ax_c1.set_title("[A] Overall Quality Frequency (OverallQual)", pad=10, fontsize=12.5, color=NAVY_PRIMARY, loc='left')
ax_c1.set_xlabel("Overall Quality Rating (1–10)", labelpad=6)
ax_c1.set_ylabel("Number of Properties", labelpad=6)
sns.despine(ax=ax_c1)

# HouseStyle Countplot
ax_c2 = axes[1]
ax_c2.set_facecolor('white')
style_order = df['HouseStyle'].value_counts().index
palette_style = sns.color_palette("crest", n_colors=len(style_order))
cp2 = sns.countplot(x='HouseStyle', data=df, order=style_order, ax=ax_c2, palette=palette_style, hue='HouseStyle', legend=False, edgecolor='#319795')
for p in cp2.patches:
    height = p.get_height()
    pct = (height / len(df)) * 100
    ax_c2.annotate(f"{int(height)}\n({pct:.1f}%)", (p.get_x() + p.get_width() / 2., height + 8),
                   ha='center', va='bottom', fontsize=8, color=GRAY_TEXT, fontweight='bold')
ax_c2.set_ylim(0, max(df['HouseStyle'].value_counts()) * 1.15)
ax_c2.set_title("[B] Architectural Dwelling Style (HouseStyle)", pad=10, fontsize=12.5, color=NAVY_PRIMARY, loc='left')
ax_c2.set_xlabel("Dwelling Style Code", labelpad=6)
ax_c2.set_ylabel("Number of Properties", labelpad=6)
ax_c2.tick_params(axis='x', rotation=30)
sns.despine(ax=ax_c2)

plt.subplots_adjust(wspace=0.22)
plt.savefig(os.path.join(other_viz_dir, 'countplots_qual_style.png'), dpi=300, facecolor='white')
plt.close()

# 5D. Scatter Key Features
print("Generating upgraded scatter_key_features.png...")
fig, axes = plt.subplots(1, 3, figsize=(19, 5.8))
fig.patch.set_facecolor('white')

# 1. GrLivArea vs SalePrice
ax_s1 = axes[0]
ax_s1.set_facecolor('white')
sns.regplot(x='GrLivArea', y='SalePrice', data=df, ax=ax_s1,
            scatter_kws={'alpha': 0.5, 'color': BLUE_SECONDARY, 's': 30, 'edgecolors': 'none'},
            line_kws={'color': CRIMSON_ALERT, 'linewidth': 2})
# Annotate famous anomalies
ax_s1.scatter([4676, 5642], [184745, 160000], color=CRIMSON_ALERT, s=80, edgecolors='black', zorder=5)
ax_s1.annotate("Atypical Sales\n(Id 524 & 1299)", xy=(5642, 160000), xytext=(4300, 280000),
               arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", color=CRIMSON_ALERT, lw=1.5),
               fontsize=8.5, fontweight='bold', color=CRIMSON_ALERT,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='#FED7D7', edgecolor='#FEB2B2', alpha=0.9))
ax_s1.set_title("[A] GrLivArea vs SalePrice (r = +0.709)", pad=10, fontsize=12.5, color=NAVY_PRIMARY, loc='left')
ax_s1.set_xlabel("Above Ground Living Area (sq ft)", labelpad=6)
ax_s1.set_ylabel("Sale Price ($ USD)", labelpad=6)
ax_s1.xaxis.set_major_formatter(comma_formatter)
ax_s1.yaxis.set_major_formatter(curr_formatter)
sns.despine(ax=ax_s1)

# 2. TotalBsmtSF vs SalePrice
ax_s2 = axes[1]
ax_s2.set_facecolor('white')
sns.regplot(x='TotalBsmtSF', y='SalePrice', data=df, ax=ax_s2,
            scatter_kws={'alpha': 0.5, 'color': TEAL_ACCENT, 's': 30, 'edgecolors': 'none'},
            line_kws={'color': NAVY_PRIMARY, 'linewidth': 2})
ax_s2.set_title("[B] TotalBsmtSF vs SalePrice (r = +0.614)", pad=10, fontsize=12.5, color=NAVY_PRIMARY, loc='left')
ax_s2.set_xlabel("Total Basement Area (sq ft)", labelpad=6)
ax_s2.set_ylabel("Sale Price ($ USD)", labelpad=6)
ax_s2.xaxis.set_major_formatter(comma_formatter)
ax_s2.yaxis.set_major_formatter(curr_formatter)
sns.despine(ax=ax_s2)

# 3. YearBuilt vs SalePrice
ax_s3 = axes[2]
ax_s3.set_facecolor('white')
sns.regplot(x='YearBuilt', y='SalePrice', data=df, ax=ax_s3,
            scatter_kws={'alpha': 0.5, 'color': CORAL_ACCENT, 's': 30, 'edgecolors': 'none'},
            line_kws={'color': NAVY_PRIMARY, 'linewidth': 2})
ax_s3.set_title("[C] YearBuilt vs SalePrice (r = +0.523)", pad=10, fontsize=12.5, color=NAVY_PRIMARY, loc='left')
ax_s3.set_xlabel("Original Construction Year", labelpad=6)
ax_s3.set_ylabel("Sale Price ($ USD)", labelpad=6)
ax_s3.yaxis.set_major_formatter(curr_formatter)
sns.despine(ax=ax_s3)

plt.subplots_adjust(wspace=0.25)
plt.savefig(os.path.join(other_viz_dir, 'scatter_key_features.png'), dpi=300, facecolor='white')
plt.close()

# 5E. Pairplot Key Features
print("Generating upgraded pairplot_key_features.png...")
pairplot_vars = ['SalePrice', 'GrLivArea', 'TotalBsmtSF', 'GarageArea', 'YearBuilt']
g = sns.PairGrid(df[pairplot_vars].dropna(), diag_sharey=False, corner=True)
g.map_lower(sns.scatterplot, alpha=0.45, s=22, color=BLUE_SECONDARY, edgecolor='none')
g.map_diag(sns.kdeplot, fill=True, color=NAVY_PRIMARY, alpha=0.6, linewidth=1.8)

# Format axes
for i, row_var in enumerate(pairplot_vars):
    for j, col_var in enumerate(pairplot_vars):
        if i >= j and g.axes[i, j] is not None:
            ax_sub = g.axes[i, j]
            if 'Price' in col_var:
                ax_sub.xaxis.set_major_formatter(curr_formatter)
            elif 'Area' in col_var or 'SF' in col_var:
                ax_sub.xaxis.set_major_formatter(comma_formatter)
            if 'Price' in row_var and j == 0:
                ax_sub.yaxis.set_major_formatter(curr_formatter)
            elif ('Area' in row_var or 'SF' in row_var) and j == 0:
                ax_sub.yaxis.set_major_formatter(comma_formatter)

g.fig.suptitle("Multivariate Pairwise Distribution Grid (Structural Covariates)", y=1.02, fontsize=15, fontweight='bold', color=NAVY_PRIMARY)
g.savefig(os.path.join(other_viz_dir, 'pairplot_key_features.png'), dpi=300, facecolor='white')
plt.close()

# 5F. Missing Values Bar Chart
print("Generating upgraded missing_values_bar.png...")
missing_series = df.isnull().sum()
missing_pct = (missing_series / len(df)) * 100
missing_df = pd.DataFrame({'Missing_Count': missing_series, 'Percentage': missing_pct})
missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values(by='Percentage', ascending=True)

fig, ax = plt.subplots(figsize=(10, 6.5))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Color code bars: High missingness (>80% feature absence) vs Imputable (<20%)
colors_m = [CORAL_ACCENT if p > 80 else (TEAL_ACCENT if p < 20 else BLUE_SECONDARY) for p in missing_df['Percentage']]
bars_m = ax.barh(missing_df.index, missing_df['Percentage'], color=colors_m, edgecolor='none', height=0.7)

for bar, (cnt, pct) in zip(bars_m, zip(missing_df['Missing_Count'], missing_df['Percentage'])):
    ax.text(pct + 1.2, bar.get_y() + bar.get_height()/2, f"{pct:.1f}% ({cnt:,})",
            va='center', ha='left', fontsize=8.5, fontweight='bold', color=NAVY_PRIMARY)

ax.set_xlim(0, 115)
ax.set_title("Missing Value Incidence Across Raw Features (% of 1,460 Records)\n", fontsize=13.5, fontweight='bold', color=NAVY_PRIMARY, loc='left')
fig.text(0.125, 0.91, "Coral: Physical amenity absence (>80%) | Teal: Standard missing measurements (<20%)", fontsize=9.5, color=GRAY_MUTED)
ax.set_xlabel("Missingness Percentage (%)", labelpad=8)
ax.set_ylabel("Attribute Name", labelpad=8)
sns.despine(ax=ax)

plt.tight_layout()
plt.savefig(os.path.join(other_viz_dir, 'missing_values_bar.png'), dpi=300, facecolor='white')
plt.close()

print("All upgraded visualizations generated successfully!")
