import pandas as pd
import os

def load_and_clean_data(file_name):
    """
    Standardizes data loading from the data/raw directory.
    """
    # 1. Construct the path (works on Ubuntu and Colab if structure is kept)
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, '../data/raw', file_name)
    
    print(f"--- Loading data from: {data_path} ---")
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Missing file: {data_path}")

    # 2. Load the data
    df = pd.read_csv(data_path)

    # 3. Simple Cleaning (Example: Remove duplicates)
    initial_count = len(df)
    df = df.drop_duplicates()
    
    if len(df) < initial_count:
        print(f"Removed {initial_count - len(df)} duplicate rows.")

    return df

if __name__ == "__main__":
    # This part only runs if you execute the script directly (for testing)
    print("Testing data loader...")
    # df = load_and_clean_data("your_dataset.csv")