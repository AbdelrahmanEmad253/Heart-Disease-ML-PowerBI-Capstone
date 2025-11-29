import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# --- Configuration ---
# 1. PASTE YOUR FOLDER PATH HERE:
data_folder_path = r"E:\courses\depi\final project\part3"

# 2. Define filenames
failure_filename = 'heart_failure_clinical_records.csv'
output_plot_C = 'failure_risk_factors_plot.png'
output_csv_C = 'failure_feature_importance.csv'

# 3. Create full file paths
failure_filepath = os.path.join(data_folder_path, failure_filename)
plot_filepath_C = os.path.join(data_folder_path, output_plot_C)
csv_filepath_C = os.path.join(data_folder_path, output_csv_C)
# ---------------------

print("--- Building Model C from 'heart_failure_clinical_records.csv' ---")

if not os.path.exists(failure_filepath):
    print(f"Error: '{failure_filename}' not found at path: {failure_filepath}")
else:
    try:
        df_failure = pd.read_csv(failure_filepath)

        # 1. Define Features (X) and Target (y)
        y = df_failure['DEATH_EVENT']
        X = df_failure.drop('DEATH_EVENT', axis=1)
        
        # 2. Split Data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        print(f"Data split complete. Training set has {len(X_train)} records.")

        # 3. Train Model
        print("Training Random Forest model (Model C)...")
        model_C = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        model_C.fit(X_train, y_train)
        print("Model training complete.")

        # 4. Evaluate Model
        y_pred = model_C.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"\n--- Model C Performance ---")
        print(f"Model Accuracy on Test Data: {accuracy * 100:.2f}%")

        # 5. Extract Insights (Feature Importance)
        print("\n--- Top 10 Prognosis Factors (Model C) ---")
        importances = model_C.feature_importances_
        feature_imp_C = pd.DataFrame(sorted(zip(importances, X.columns)), columns=['Importance', 'Feature'])
        feature_imp_C = feature_imp_C.sort_values(by="Importance", ascending=False)

        print(feature_imp_C.head(10).to_markdown(index=False, numalign="left", stralign="left"))
        
        # Save the full importance list
        feature_imp_C.to_csv(csv_filepath_C, index=False)
        print(f"\nSaved feature importance to '{csv_filepath_C}'")
        
        # 6. Create and save bar plot
        plt.figure(figsize=(10, 8))
        sns.barplot(x='Importance', y='Feature', data=feature_imp_C, palette='cubehelix')
        plt.title('Key Prognosis Factors for Heart Failure (from heart_failure_clinical_records.csv)', fontsize=16)
        plt.xlabel('Importance Score', fontsize=12)
        plt.ylabel('Clinical Feature', fontsize=12)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        
        plt.savefig(plot_filepath_C)
        print(f"Successfully created and saved '{output_plot_C}'")

    except Exception as e:
        print(f"An error occurred: {e}")