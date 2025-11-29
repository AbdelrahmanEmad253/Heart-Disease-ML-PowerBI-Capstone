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
cardio_filename = 'cardio_train.csv'
output_plot_B = 'cardio_risk_factors_plot.png'
output_csv_B = 'cardio_feature_importance.csv'

# 3. Create full file paths
cardio_filepath = os.path.join(data_folder_path, cardio_filename)
plot_filepath_B = os.path.join(data_folder_path, output_plot_B)
csv_filepath_B = os.path.join(data_folder_path, output_csv_B)
# ---------------------

print("--- Building Model B from 'cardio_train.csv' ---")

if not os.path.exists(cardio_filepath):
    print(f"Error: '{cardio_filename}' not found at path: {cardio_filepath}")
else:
    try:
        df_cardio = pd.read_csv(cardio_filepath, delimiter=';')

        # --- 1. Preprocessing ---
        print("Preprocessing data (dropping 'id', converting 'age' to years)...")
        if 'id' in df_cardio.columns:
            df_cardio = df_cardio.drop('id', axis=1)
        if 'age' in df_cardio.columns:
            df_cardio['age_years'] = (df_cardio['age'] / 365.25).round().astype(int)
            df_cardio = df_cardio.drop('age', axis=1) 
        print("Preprocessing complete.")

        # 2. Define Features (X) and Target (y)
        y = df_cardio['cardio']
        X = df_cardio.drop('cardio', axis=1)
        
        # 3. Split Data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        print(f"\nData split complete. Training set has {len(X_train)} records.")

        # 4. Train Model
        print("Training Random Forest model (Model B)...")
        model_B = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        model_B.fit(X_train, y_train)
        print("Model training complete.")

        # 5. Evaluate Model
        y_pred = model_B.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"\n--- Model B Performance ---")
        print(f"Model Accuracy on Test Data: {accuracy * 100:.2f}%")

        # 6. Extract Insights (Feature Importance)
        print("\n--- Top 10 Clinical Factors (Model B) ---")
        importances = model_B.feature_importances_
        feature_imp_B = pd.DataFrame(sorted(zip(importances, X.columns)), columns=['Importance', 'Feature'])
        feature_imp_B = feature_imp_B.sort_values(by="Importance", ascending=False)

        print(feature_imp_B.head(10).to_markdown(index=False, numalign="left", stralign="left"))
        
        # Save the full importance list
        feature_imp_B.to_csv(csv_filepath_B, index=False)
        print(f"\nSaved feature importance to '{csv_filepath_B}'")

        # 7. Create and save bar plot
        plt.figure(figsize=(10, 8))
        sns.barplot(x='Importance', y='Feature', data=feature_imp_B, palette='viridis')
        plt.title('General Checkup Risk Factors (from cardio_train.csv)', fontsize=16)
        plt.xlabel('Importance Score', fontsize=12)
        plt.ylabel('Clinical Feature', fontsize=12)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        
        plt.savefig(plot_filepath_B)
        print(f"Successfully created and saved '{output_plot_B}'")

    except Exception as e:
        print(f"An error occurred: {e}")