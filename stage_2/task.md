# 📌 Task Code 2.1: Microbiology Analysis

## **Dataset Overview**
Look at this dataset **[https://raw.githubusercontent.com/HackBio-Internship/public_datasets/refs/heads/main/R/iris_downloaded.csv]** (open in a new tab, not a file to be downloaded). This dataset contains **OD600 (Optical Density at 600 nm) vs Time** for different bacterial strains.

## **Objective**
The goal of this task is to analyze bacterial growth curves and compare the growth patterns of **knock-out (-) strains** and **knock-in (+) strains**.

## **Tasks**
### **1️⃣ Plot Growth Curves**
- For each strain, plot a **growth curve** of:
  - Knock-out (-) strain
  - Knock-in (+) strain
- Overlay both on the same plot to compare their growth patterns.

### **2️⃣ Determine Time to Carrying Capacity**
- Use your function from the last stage to determine **the time required to reach carrying capacity (K)** for each strain/mutant.

### **3️⃣ Scatter Plot: Time to Carrying Capacity**
- Generate a **scatter plot** comparing the time it takes to reach carrying capacity for:
  - Knock-out (-) strains
  - Knock-in (+) strains

### **4️⃣ Box Plot: Time to Carrying Capacity**
- Generate a **box plot** to visualize the **distribution** of time taken by:
  - Knock-out (-) strains
  - Knock-in (+) strains

### **5️⃣ Statistical Analysis**
- Determine whether there is a **statistical difference** in the time it takes for knock-out (-) strains to reach carrying capacity compared to knock-in (+) strains.
- Use statistical tests (e.g., **t-test**) to assess significance.

### **6️⃣ Observations & Analysis**
- Analyze the plots and statistical results.
- Explain your **observations as comments** in your code.

## **Expected Deliverables**
- Growth curves for each strain.
- Scatter and box plots for carrying capacity time.
- Statistical analysis results.
- Documented observations in your code.

## **Tools & Libraries**
You may use **Python** with the following libraries:
- `pandas` for data handling
- `matplotlib` for visualization
- `seaborn` for enhanced plotting
- `scipy.stats` for statistical analysis

## **Next Steps**
1. Load and explore the dataset.
2. Implement the required plots and calculations.
3. Document observations and submit results.  



# 📌 Task Code 2.3: Botany and Plant Science Analysis

## Overview
This project analyzes the metabolic response of engineered mutant crops compared to wild-type (WT) plants when exposed to a pesticide. The study examines changes in metabolic response over time and identifies significant variations using statistical and visualization techniques.

## Dataset
- **Source**: [Dataset Link](https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv)
- **Description**: Contains metabolic response measurements for WT and mutant plants at different time points (0h, 8h, and 24h) under DMSO treatment.

## Objectives
1. **Calculate the metabolic response difference (ΔM)**
   - Compute the difference in metabolic response between the 24-hour treatment and the DMSO treatment for both WT and mutant plants.

2. **Scatter Plot for ΔM**
   - Generate a scatter plot comparing ΔM values for WT and mutant plants.
   - Fit a reference line with a y-intercept of 0 and a slope of 1.

3. **Residual Analysis**
   - Calculate the residuals (difference between the fitted line and each point).
   - Define a cut-off value (e.g., 0.3) to classify metabolites:
     - **Grey**: Residuals within ±n (e.g., ±0.3)
     - **Salmon**: Residuals outside this range
   - Identify and list metabolites that fall outside the cut-off range.

4. **Line Plot for Selected Metabolites**
   - Select six metabolites that fall outside the cut-off range.
   - Generate line plots showing metabolic response over time (0h, 8h, 24h).

## Interpretation & Insights
- Analyze trends in metabolic response changes.
- Discuss implications of significant deviations in metabolic activity.
- Explain the role of metabolites with extreme responses in pesticide resistance.

## Tools & Libraries Used
- **Python**
  - `pandas` for data processing
  - `matplotlib` & `seaborn` for visualization
  - `numpy` for numerical computations

## Expected Output
- A scatter plot with categorized metabolites
- A table of metabolites falling outside the residual threshold
- Line plots of selected metabolites over time
- Observations and interpretations from the data analysis

## How to Run the Analysis
1. Install dependencies:
   ```sh
   pip install pandas matplotlib seaborn numpy
   ```
2. Load and process the dataset.
3. Compute ΔM and residuals.
4. Generate plots and interpret results.

## Conclusion
This study helps understand metabolic adaptations in engineered plants and can contribute to improving crop resistance to pesticides.

🚀 **Happy Coding!**

