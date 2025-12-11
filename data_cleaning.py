import pandas as pd
import os

# --- Configuration ---
# Get the absolute path of the script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# The script is located at the repository root, so 'data' is a subdirectory here
DATA_DIR = os.path.join(SCRIPT_DIR, 'data')

# Update these filenames based on your actual data
INPUT_FILENAME = 'dataset-raw.csv' 
OUTPUT_FILENAME = 'dataset-cleaned.csv'

INPUT_PATH = os.path.join(DATA_DIR, INPUT_FILENAME)
OUTPUT_PATH = os.path.join(DATA_DIR, OUTPUT_FILENAME)

def load_data(filepath):
    """Loads the raw dataset."""
    try:
        print(f"Loading data from: {filepath}")
        df = pd.read_csv(filepath)
        print(f"Successfully loaded {len(df)} rows.")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Please check the filename in the 'data' folder.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """
    Main function to clean the dataframe.
    """
    if df is None:
        return None

    print("\n--- Starting Data Cleaning ---")
    
    # 1. Create a copy to avoid SettingWithCopy warnings
    df = df.copy()

    # 2. Standardize Column Names (snake_case)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # 3. Remove Duplicates
    duplicates = df[df.duplicated()]
    if not duplicates.empty:
        print(f"Found {len(duplicates)} duplicate rows.")
        print("Sample of duplicates:")
        print(duplicates.head())
        initial_rows = len(df)
        df.drop_duplicates(inplace=True)
        print(f"Removed {initial_rows - len(df)} duplicate rows.")
    else:
        print("No duplicate rows found.")

    # 4. Handle Missing Values (Example logic)
    # print("Missing values per column:")
    # print(df.isnull().sum())
    # df.dropna(subset=['track_id'], inplace=True) # Example: Drop if ID is missing

    print("--- Data Cleaning Completed ---\n")
    return df

def save_data(df, filepath):
    """Saves the cleaned dataset."""
    if df is not None:
        try:
            df.to_csv(filepath, index=False)
            print(f"Cleaned data saved to: {filepath}")
        except Exception as e:
            print(f"Error saving data: {e}")

def main():
    # Ensure data directory exists
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    df = load_data(INPUT_PATH)
    df_cleaned = clean_data(df)
    save_data(df_cleaned, OUTPUT_PATH)

if __name__ == "__main__":
    main()