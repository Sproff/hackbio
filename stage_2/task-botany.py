import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (tsv = tab-separated values)
url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv"
df = pd.read_csv(url, sep="\t")

# Display first few rows to understand the structure of the dataset
# print(df.head())

# Extract time column
time = df["time"]

# Identify strains (all columns except 'time')
strains = df.columns[1:]

# Define WT (Wild Type) and MUT (Mutant) strains
wt_strains = [
    "A1",
    "A3",
    "A5",
    "A7",
    "A9",
    "A11",
    "B1",
    "B3",
    "B5",
    "B7",
    "B9",
    "B11",
    "C1",
    "C3",
    "C5",
    "C7",
    "C9",
    "C11",
]
mut_strains = [
    "A2",
    "A4",
    "A6",
    "A8",
    "A10",
    "A12",
    "B2",
    "B4",
    "B6",
    "B8",
    "B10",
    "B12",
    "C2",
    "C4",
    "C6",
    "C8",
    "C10",
    "C12",
]


# 1️. Compute ΔM (Difference in Metabolic Response)
dmso_values = df[wt_strains]  # Dimethyl Sulfoxide (DMSO) treatment for WT
mut_values_24h = df[mut_strains]  # 24-hour treatment for Mutants
delta_m_numpy_arr = mut_values_24h.mean().values - dmso_values.mean().values
print(delta_m_numpy_arr)

# Convert to pd series seince we are woring with pd and the result came out a s a numpy array
delta_m_pd_series = pd.Series(delta_m_numpy_arr, index=dmso_values.columns)
print(delta_m_pd_series)

# 2️. Scatter plot of ΔM for WT and Mutants
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x=dmso_values.mean(),
    y=mut_values_24h.mean(),
    hue=["Metabolic Response"] * len(dmso_values.mean()),  # Fix legend issue
    legend="full",
)
plt.plot(
    [0, max(dmso_values.mean())], [0, max(mut_values_24h.mean())], "r--", label="y = x"
)
plt.xlabel("DMSO Metabolic Response (WT)")
plt.ylabel("24h Metabolic Response (Mutants)")
plt.title("Scatter Plot of ΔM (Metabolic Response Difference)")
plt.legend()
plt.show()

# 3️. Compute residuals and color points based on cutoff
cutoff = 0.3  # Define cutoff threshold
residuals = mut_values_24h.mean() - dmso_values.mean()

# Convert colors into a Pandas categorical series
colors = pd.Series(
    ["salmon" if abs(res) > cutoff else "grey" for res in residuals], dtype="category"
)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=dmso_values.mean(), y=mut_values_24h.mean(), hue=colors, legend=False)
plt.plot(
    [0, max(dmso_values.mean())], [0, max(mut_values_24h.mean())], "r--", label="y = x"
)
plt.xlabel("DMSO Metabolic Response (WT)")
plt.ylabel("24h Metabolic Response (Mutants)")
plt.title("Scatter Plot with Residual Coloring")

# Manually add legend
legend_labels = [
    Patch(color="salmon", label="Significant Change"),
    Patch(color="grey", label="Non-significant"),
]
plt.legend(handles=legend_labels)
plt.show()

# 4️. Identify and plot 6 metabolites that fall outside the residual cutoff
outliers = residuals[abs(residuals) > cutoff].index[:6]

plt.figure(figsize=(10, 6))
for metabolite in outliers:
    plt.plot(
        [0, 8, 24],
        df.loc[df["time"].isin([0, 8, 24]), metabolite],
        marker="o",
        label=metabolite,
    )
plt.xlabel("Time (hours)")
plt.ylabel("Metabolic Response")
plt.title("Metabolic Response Trends for Outlier Metabolites")
plt.legend()
plt.show()
