import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# --- Configuration ---
# 1. PASTE YOUR FOLDER PATH HERE:
data_folder_path = r"E:\courses\depi\final project\part2"

# 2. Define filenames
heart_filename = 'heart.csv'
output_plot_A = 'heart_risk_factors_plot.png'
output_csv_A = 'heart_feature_importance.csv'

# 3. Create full file paths
heart_filepath = os.path.join(data_folder_path, heart_filename)
plot_filepath_A = os.path.join(data_folder_path, output_plot_A)
csv_filepath_A = os.path.join(data_folder_path, output_csv_A)
# ---------------------

print("--- Building Model A from 'heart.csv' ---")

if not os.path.exists(heart_filepath):
    print(f"Error: '{heart_filename}' not found at path: {heart_filepath}")
else:
    try:
        df_heart = pd.read_csv(heart_filepath)

        # 1. Define Features (X) and Target (y)
        y = df_heart['target']
        X = df_heart.drop('target', axis=1)
        
        # 2. Split Data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        print(f"Data split complete. Training set has {len(X_train)} records.")

        # 3. Train Model
        print("Training Random Forest model (Model A)...")
        model_A = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        model_A.fit(X_train, y_train)
        print("Model training complete.")

        # 4. Evaluate Model
        y_pred = model_A.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"\n--- Model A Performance ---")
        print(f"Model Accuracy on Test Data: {accuracy * 100:.2f}%")

        # 5. Extract Insights (Feature Importance)
        print("\n--- Top 10 Clinical Factors (Model A) ---")
        importances = model_A.feature_importances_
        feature_imp = pd.DataFrame(sorted(zip(importances, X.columns)), columns=['Importance', 'Feature'])
        feature_imp = feature_imp.sort_values(by="Importance", ascending=False)
        
        print(feature_imp.head(10).to_markdown(index=False, numalign="left", stralign="left"))
        
        # Save the full importance list
        feature_imp.to_csv(csv_filepath_A, index=False)
        print(f"\nSaved feature importance to '{csv_filepath_A}'")
        
        # 6. Create and save bar plot
        plt.figure(figsize=(10, 8))
        sns.barplot(x='Importance', y='Feature', data=feature_imp, palette='plasma')
        plt.title('Clinical Risk Factors for Heart Disease (from heart.csv)', fontsize=16)
        plt.xlabel('Importance Score', fontsize=12)
        plt.ylabel('Clinical Feature', fontsize=12)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        
        plt.savefig(plot_filepath_A)
        print(f"Successfully created and saved '{output_plot_A}'")

    except Exception as e:
        print(f"An error occurred: {e}")