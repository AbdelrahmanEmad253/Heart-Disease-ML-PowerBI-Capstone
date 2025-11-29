import pandas as pd

# Load the dataset
try:
    df_cvd = pd.read_csv('CVD_cleaned.csv')

    # 1. Inspect the first 5 rows
    print("--- First 5 Rows (head) ---")
    print(df_cvd.head().to_markdown(index=False, numalign="left", stralign="left"))

    # 2. Review column names, data types, and non-null counts
    print("\n--- Column Info (info) ---")
    # Using a string buffer to capture the .info() output to print it
    import io
    buf = io.StringIO()
    df_cvd.info(buf=buf)
    print(buf.getvalue())

    # 3. Check for missing values
    print("\n--- Missing Values (isnull.sum) ---")
    print(df_cvd.isnull().sum().to_markdown(numalign="left", stralign="left"))

except FileNotFoundError:
    print("Error: The file 'CVD_cleaned.csv' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
############################################################################################################################################
import pandas as pd

# Load the dataset
try:
    df_cvd = pd.read_csv('CVD_cleaned.csv')

    # Get a list of all columns that are of type 'object' (text)
    object_cols = df_cvd.select_dtypes(include=['object']).columns

    print("--- Unique Values in 'object' (text) Columns ---")
    
    # Loop through each object column and print its unique values
    for col in object_cols:
        print(f"\nColumn: '{col}'")
        unique_values = df_cvd[col].unique()
        print(unique_values)

except FileNotFoundError:
    print("Error: The file 'CVD_cleaned.csv' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
############################################################################################################################################
import pandas as pd

# Load the dataset
try:
    df_cvd = pd.read_csv('CVD_cleaned.csv')
    print("--- Original Dtypes (Partial) ---")
    print(df_cvd[['General_Health', 'Heart_Disease', 'Sex', 'Age_Category', 'Diabetes']].dtypes)

    # 1. Define Binary Mappings
    # (Simple Yes/No and Male/Female)
    binary_map = {
        'No': 0, 'Yes': 1,
        'Female': 0, 'Male': 1
    }
    binary_cols = ['Exercise', 'Heart_Disease', 'Skin_Cancer', 'Other_Cancer', 'Depression', 'Arthritis', 'Sex', 'Smoking_History']
    
    for col in binary_cols:
        df_cvd[col] = df_cvd[col].map(binary_map)

    # 2. Define Ordinal (Ranked) Mappings
    health_map = {
        'Poor': 0, 'Fair': 1, 'Good': 2, 'Very Good': 3, 'Excellent': 4
    }
    checkup_map = {
        'Never': 0, '5 or more years ago': 1, 'Within the past 5 years': 2, 'Within the past 2 years': 3, 'Within the past year': 4
    }
    age_map = {
        '18-24': 0, '25-29': 1, '30-34': 2, '35-39': 3, '40-44': 4, '45-49': 5,
        '50-54': 6, '55-59': 7, '60-64': 8, '65-69': 9, '70-74': 10, '75-79': 11, '80+': 12
    }
    
    df_cvd['General_Health'] = df_cvd['General_Health'].map(health_map)
    df_cvd['Checkup'] = df_cvd['Checkup'].map(checkup_map)
    df_cvd['Age_Category'] = df_cvd['Age_Category'].map(age_map)

    # 3. One-Hot Encoding for 'Diabetes'
    # This creates new columns for each category and drops the original
    df_cvd = pd.get_dummies(df_cvd, columns=['Diabetes'], prefix='Diabetes')

    # 4. Verification
    print("\n--- New Dtypes (Verification) ---")
    import io
    buf = io.StringIO()
    df_cvd.info(buf=buf)
    print(buf.getvalue())

    print("\n--- Transformed Data (Head) ---")
    print(df_cvd.head().to_markdown(index=False, numalign="left", stralign="left"))
    
    # Save the processed file for future use (and for Power BI)
    processed_filename = "CVD_processed_for_model.csv"
    df_cvd.to_csv(processed_filename, index=False)
    print(f"\nSuccessfully saved processed data to '{processed_filename}'")

except FileNotFoundError:
    print("Error: The file 'CVD_cleaned.csv' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
############################################################################################################################################

