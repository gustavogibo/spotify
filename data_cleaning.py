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

def standardize_columns(df):
    """Standardizes column names to snake_case."""
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    
    # Remove 'unnamed:_0' if it exists (common artifact)
    if 'unnamed:_0' in df.columns:
        df.drop(columns=['unnamed:_0'], inplace=True)
        print("Dropped 'unnamed:_0' column.")

    print("Columns after standardization:")
    print(list(df.columns))
    return df

def remove_duplicates(df):
    """Checks for and removes duplicate rows."""
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
    return df

def handle_missing_values(df):
    """Checks for missing values and removes rows with missing core data."""
    missing_values = df.isnull().sum()
    if missing_values.sum() > 0:
        print("\nMissing values found per column:")
        print(missing_values[missing_values > 0])
    else:
        print("\nNo missing values found.")

    # Remove rows where track_name or album_name are missing
    subset_cols = ['track_name', 'album_name']
    existing_subset = [col for col in subset_cols if col in df.columns]
    
    if existing_subset:
        initial_rows = len(df)
        df.dropna(subset=existing_subset, inplace=True)
        dropped = initial_rows - len(df)
        if dropped > 0:
            print(f"Dropped {dropped} rows where { ' or '.join(existing_subset) } were missing.")

    return df

def clean_data(df):
    """
    Main function to clean the dataframe.
    """
    if df is None:
        return None

    print("\n--- Starting Data Cleaning ---")
    
    # 1. Create a copy to avoid SettingWithCopy warnings
    df = df.copy()

    # Apply cleaning steps
    df = standardize_columns(df)
    df = remove_duplicates(df)
    df = handle_missing_values(df)

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