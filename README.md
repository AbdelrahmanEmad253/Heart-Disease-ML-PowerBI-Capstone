# Machine Learning for Heart Disease: Prevention, Diagnosis, and Prognosis

## 📌 Project Overview
This project is a comprehensive machine learning analysis of cardiovascular disease (CVD). It leverages four distinct datasets to analyze the "Patient Journey" across three critical stages:
1.  **Prevention:** Identifying lifestyle risk factors in the general population.
2.  **Diagnosis:** Comparing predictors for general screening vs. detailed clinical diagnosis.
3.  **Prognosis:** Predicting survival outcomes for heart failure patients.

Built as a team capstone at the DEPI program.

The project includes a complete **ETL pipeline**, **Machine Learning modeling (Random Forest)**, and an interactive **Power BI Dashboard**.

## 🛠️ Tech Stack
* **Python:** Pandas (Cleaning), Scikit-learn (ML Modeling), Matplotlib/Seaborn (Visualization).
* **Power BI:** Data Modeling, DAX, Interactive Dashboarding.
* **Machine Learning:** Random Forest Classifier.

## 📂 Project Structure
* `scripts/`: Python scripts for Preprocessing, EDA, and Model Training.
* `datasets/`: The four datasets used for analysis.
* `outputs/`: Generated feature importance rankings and static plots.
* `dashboard/`: The final Power BI (.pbix) file and PDF export.

## 📊 Key Findings

### Part 1: Prevention (Lifestyle)
* **Accuracy:** 91.90%
* **Insight:** **BMI** and **Weight** are the strongest predictors of heart disease risk in the general population, outweighing other lifestyle factors.

### Part 2: Diagnosis (Clinical)
* **Detailed Diagnosis:** 100% Accuracy (original single split; 82.5% under deduplicated 5-fold CV, see limitations) using Stress Test results (`Chest Pain`, `Max Heart Rate`).
* **General Screening:** 70.6% Accuracy using basic metrics (`Blood Pressure`, `BMI`).

### Part 3: Prognosis (Survival)
* **Accuracy:** 99.10% (original single split; 93.9% without `time` under deduplicated 5-fold CV, see limitations)
* **Insight:** Survival is determined by **Time** (follow-up duration), **Kidney Function** (Serum Creatinine), and **Heart Function** (Ejection Fraction). Lifestyle factors have minimal impact at this late stage.

## 📈 Power BI Dashboard
The project concludes with a 4-page interactive dashboard allowing users to explore the shift from lifestyle-driven risks to organ-function-driven risks.

See `dashboard/Final Project - Vis[1].pdf` for an export.

## ⚠️ Limitations & honest notes
Originally reported numbers (single 80/20 split): prognosis **99.1%**, diagnosis **100%**. These were re-checked with 5-fold stratified CV (`scripts/cv_eval.py`, same Random Forest settings, results in `outputs/cv_results.md`), reporting accuracy, recall and ROC-AUC as mean ± std:

| Task | Features | Deduplicated | Rows | Accuracy | Recall | ROC-AUC |
|---|---|---|---|---|---|---|
| Prognosis | all features incl. time | no | 5000 | 0.992 ± 0.002 | 0.980 ± 0.004 | 1.000 ± 0.000 |
| Prognosis | all features incl. time | yes | 1320 | 0.958 ± 0.011 | 0.894 ± 0.030 | 0.990 ± 0.009 |
| Prognosis | without time | no | 5000 | 0.989 ± 0.001 | 0.974 ± 0.004 | 0.999 ± 0.000 |
| Prognosis | without time | yes | 1320 | 0.939 ± 0.011 | 0.854 ± 0.027 | 0.979 ± 0.006 |
| Diagnosis | all features | no | 1025 | 0.996 ± 0.008 | 0.992 ± 0.015 | 1.000 ± 0.000 |
| Diagnosis | all features | yes | 302 | 0.825 ± 0.033 | 0.854 ± 0.073 | 0.907 ± 0.011 |

**Headline (deduplicated 5-fold CV):** prognosis without `time` = 93.9% accuracy, 85.4% recall, 0.979 ROC-AUC; diagnosis = 82.5% accuracy, 85.4% recall, 0.907 ROC-AUC.

**Why this changed:**
- **Duplicate rows across train/test.** `heart.csv` has 1025 rows but only 302 unique; `heart_failure_clinical_records.csv` has 5000 rows but only 1320 unique. With a random split, copies of the same patient land in both train and test, so the model is partly scored on rows it has memorised. Deduplicating before splitting drops diagnosis from ~99.6% to 82.5%.
- **`time` leakage.** `time` (follow-up duration) is only known after the outcome, so it leaks the target. Removing it lowers deduplicated prognosis accuracy from 95.8% to 93.9%.
- Accuracy alone hides errors on imbalanced medical data, so recall (sensitivity) and ROC-AUC are reported too: missing a sick patient costs more than a false alarm.

## 🚀 How to Run
1.  Install dependencies: `pip install -r requirements.txt`
2.  Run the scripts in the `scripts/` folder to generate models and insights.
3.  Open `dashboard/Final Project - Vis.pbix` in Power BI Desktop.
