import os
import glob
import pandas as pd

# ✅ Define Paths
PROJECT_PATH = r"C:\Users\prita\OneDrive\Desktop\Ev_charging"
DATASET_PATH = os.path.join(PROJECT_PATH, "dataset")
PROCESSED_DATA_PATH = os.path.join(PROJECT_PATH, "processed_data")

# ✅ Ensure processed_data folder exists
os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

# ✅ Function to Load CSV File with Debugging
def load_csv(file_path, file_name):
    """Loads a CSV file if it exists, else returns None."""
    full_path = os.path.join(file_path, file_name)
    if os.path.exists(full_path):
        df = pd.read_csv(full_path)
        print(f"✅ Loaded: {file_name}, Shape: {df.shape}")
        return df
    else:
        print(f"❌ File Not Found: {full_path}")
        return None

# ✅ List of Datasets to Load (Outside EV Consumption)
datasets = {
    "air_quality": "air_quality.csv",
    "geolocation": "geolocation_hyderabad.csv",
    "land_use": "land_use_hyderabad.csv",
    "population_density": "population_density.csv",
    "road_network": "road_network.csv",
    "ev_registration_date": "ev_registration_date.csv"
}

# ✅ Load Each Dataset
dataframes = {name: load_csv(DATASET_PATH, filename) for name, filename in datasets.items()}

# ✅ Load All EV Consumption Files from 'ev_consumption' Folder
EV_CONSUMPTION_PATH = os.path.join(DATASET_PATH, "ev_consumption")
csv_files = glob.glob(os.path.join(EV_CONSUMPTION_PATH, "*.csv"))

if not csv_files:
    print(f"❌ No EV consumption CSV files found in: {EV_CONSUMPTION_PATH}")
    dataframes["ev_consumption"] = None
else:
    ev_consumption_list = [pd.read_csv(file) for file in csv_files if os.path.getsize(file) > 0]  # Avoid empty files
    if ev_consumption_list:
        ev_consumption = pd.concat(ev_consumption_list, ignore_index=True)
        print(f"✅ Successfully concatenated {len(csv_files)} EV consumption files! Shape: {ev_consumption.shape}")
        dataframes["ev_consumption"] = ev_consumption
    else:
        print("❌ No valid data in EV consumption files.")
        dataframes["ev_consumption"] = None

# ✅ Print Sample Data (Optional Debugging)
for name, df in dataframes.items():
    if df is not None:
        print(f"\n🔹 {name} Data Sample:")
        print(df.head())

# ✅ Save Preprocessed Data
for name, df in dataframes.items():
    if df is not None:
        processed_file = os.path.join(PROCESSED_DATA_PATH, f"{name}_processed.csv")
        df.to_csv(processed_file, index=False)
        print(f"✅ {name} Data Saved: {processed_file}")

print("\n🎉 Data Preprocessing Completed Successfully!")
