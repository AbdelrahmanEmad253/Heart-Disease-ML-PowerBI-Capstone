# **Technical Documentation: Heart Disease Analysis Dashboard**

**Project Title:** Machine Learning for Heart Disease: Prevention, Diagnosis, and Prognosis 

**Tool:** Microsoft Power BI Desktop 

**Author:** ALX3\_DAT2\_S3\_T296

---

## **1\. Executive Summary**

This Power BI dashboard serves as the visualization layer for a comprehensive machine learning study on cardiovascular disease. It synthesizes insights from four distinct datasets to analyze the "Patient Journey" across three stages:

1. **Prevention:** Lifestyle risk factors in the general population.  
2. **Diagnosis:** Comparing general screening vs. detailed clinical diagnosis.  
3. **Prognosis:** Predicting survival outcomes for heart failure patients.

The dashboard integrates raw clinical data with pre-calculated machine learning insights (Feature Importance rankings) generated in Python (Random Forest Classifier).

---

## **2\. Data Architecture**

### **2.1 Data Sources**

The dashboard loads eight flat files (CSVs) organized into two categories:

**A. Primary Patient Data (Raw Clinical Records)**

* `Lifestyle Risk Data` (Source: `CVD_processed_for_model.csv`) \- 308k+ records.  
* `Detailed Diagnosis Data` (Source: `heart.csv`) \- Clinical study data.  
* `General Screening Data` (Source: `cardio_train.csv`) \- Routine checkup data.  
* `Heart Failure Prognosis Data` (Source: `heart_failure_clinical_records.csv`) \- Post-diagnosis survival data.

**B. Machine Learning Outputs (Aggregated Insights)**

* `Lifestyle Feature Importance`  
* `Detailed Diagnosis Importance`  
* `General Screening Importance`  
* `Prognosis Feature Importance`

*Note: The "Importance" tables contain the predictive score (0-1) for each feature as determined by the Random Forest model.*

### **2.2 Data Modeling Strategy**

* **Structure:** The data model utilizes a **disassociated table design** (Siloed Model).  
* **Rationale:** No relationships were created between the four primary data tables because they represent distinct patient populations and different stages of the disease lifecycle. Merging them would result in data integrity issues. Each report page functions as an independent analytical unit.

---

## **3\. ETL & Data Transformation (Power Query)**

Data cleaning and transformation were performed using Power Query Editor (M Language).

**Key Transformation Logic:**

1. **Categorical Conversion:**  
   * *Problem:* Key categorical variables (e.g., `Sex`, `Heart_Disease`, `Smoking_History`) were stored as integers (`0` and `1`) in the raw CSVs. Power BI defaulted to summarizing these (Sum/Average).  
   * *Solution:* All nominal columns were cast to **Text** data type. `0` / `1` values were preserved as text labels to function as chart dimensions (Axis/Legend) rather than values.  
2. **Feature Importance Handling:**  
   * Ensured `Importance` columns were set to **Decimal Number** and `Don't Summarize` to accurately render relative importance in bar charts.

---

## 

## 

## **4\. Calculated Measures (DAX)**

Data Analysis Expressions (DAX) were used to create dynamic KPIs. Standard aggregation functions (`COUNTROWS`, `CALCULATE`, `DIVIDE`) were used to normalize data across different sample sizes.

**Key Measures by Module:**

* **Part 1 (Prevention):** `% Heart Disease` \= `DIVIDE([Heart Disease Cases], [Total Patients])`  
* **Part 2 (Diagnosis):** `% Disease Rate (Screening)` \= `DIVIDE([Positive Cases], [Total Patients])`  
* **Part 3 (Prognosis):** `Mortality Rate` \= `DIVIDE([Death Events], [Total Heart Failure Patients])`

---

## **5\. Dashboard Design & Visual Narrative**

The dashboard is structured into a "Home" landing page and four analytical modules.

### **Home Page (Navigation)**

* **Purpose:** Central hub for user navigation.  
* **Components:** Project title, navigation buttons (`Lifestyle Risk`, `Clinical Diagnosis`, `Prognosis`, `Risk Factor Analysis`), and executive project summary.

### **Page 1: Prevention (Lifestyle Insights)**

* **Core Question:** What lifestyle factors most strongly predict heart disease?  
* **Key Visual:** Horizontal Bar Chart of `Lifestyle Feature Importance`.  
  * *Insight:* **BMI** and **Weight** are identified as the top risk drivers.  
* **Supporting Analysis:** Analysis of disease rates by `General Health` status (showing a 31% risk for "Poor" health) and `Smoking History`.

### **Page 2: Clinical Diagnosis**

* **Core Question:** How does a detailed workup compare to a general screening?  
* **Key Visual:** Side-by-side comparison of Feature Importance.  
  * *Chart A:* Shows `Chest Pain Type` and `ST Depression` drive Detailed Diagnosis (100% Accuracy).  
  * *Chart B:* Shows `Blood Pressure` and `BMI` drive General Screening (70% Accuracy).

### **Page 3: Patient Prognosis**

* **Core Question:** What determines survival after heart failure?  
* **Key Visual:** Feature Importance Chart for Mortality.  
  * *Insight:* **Time** (Follow-up duration), **Serum Creatinine** (Kidney function), and **Ejection Fraction** (Heart function) are the dominant predictors, surpassing lifestyle factors.  
* **Supporting Analysis:** Mortality risk curves by Ejection Fraction and Serum Creatinine levels.

### **Page 4: Detailed Risk Analysis**

* **Core Question:** Deep dive into specific clinical symptoms.  
* **Key Visual:** Analysis of `Chest Pain Type` impact on disease rates.  
  * *Insight:* Visualizes how specific symptoms (e.g., Asymptomatic vs. Typical Angina) correlate with the presence of heart disease in the clinical dataset.

---

## **6\. Conclusion**

This Power BI solution successfully operationalizes the findings of the machine learning models. It provides a user-friendly interface to explore the critical shift in risk factors: moving from **lifestyle-driven risks** in the general population to **organ-function-driven risks** in diagnosed patients.

