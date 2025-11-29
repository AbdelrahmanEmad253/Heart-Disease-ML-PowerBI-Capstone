# Machine Learning for Heart Disease: Prevention, Diagnosis, and Prognosis

## 📌 Project Overview
This project is a comprehensive machine learning analysis of cardiovascular disease (CVD). It leverages four distinct datasets to analyze the "Patient Journey" across three critical stages:
1.  **Prevention:** Identifying lifestyle risk factors in the general population.
2.  **Diagnosis:** Comparing predictors for general screening vs. detailed clinical diagnosis.
3.  **Prognosis:** Predicting survival outcomes for heart failure patients.

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
* **Detailed Diagnosis:** 100% Accuracy using Stress Test results (`Chest Pain`, `Max Heart Rate`).
* **General Screening:** 70.6% Accuracy using basic metrics (`Blood Pressure`, `BMI`).

### Part 3: Prognosis (Survival)
* **Accuracy:** 99.10%
* **Insight:** Survival is determined by **Time** (follow-up duration), **Kidney Function** (Serum Creatinine), and **Heart Function** (Ejection Fraction). Lifestyle factors have minimal impact at this late stage.

## 📈 Power BI Dashboard
The project concludes with a 4-page interactive dashboard allowing users to explore the shift from lifestyle-driven risks to organ-function-driven risks.

![Dashboard Preview](dashboard/Final Project - Vis.pdf) *(Note: Github will render the PDF link or you can upload a screenshot here)*

## 🚀 How to Run
1.  Install dependencies: `pip install -r requirements.txt`
2.  Run the scripts in the `scripts/` folder to generate models and insights.
3.  Open `dashboard/Final Project - Vis.pbix` in Power BI Desktop.
