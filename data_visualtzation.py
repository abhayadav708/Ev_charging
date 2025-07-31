import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Define the Correct Path
processed_data_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\processed_data"
file_name = "ev_consumption_cleaned.csv"

# ✅ Load the Processed EV Consumption Data
file_path = os.path.join(processed_data_path, file_name)

if os.path.exists(file_path):
    ev_consumption = pd.read_csv(file_path)
    print(f"✅ EV Consumption Data Loaded! Shape: {ev_consumption.shape}")
else:
    print(f"❌ Error: File '{file_name}' not found in '{processed_data_path}'")
    exit()

# ✅ Ensure "units" Column Exists
required_column = "units"

if required_column not in ev_consumption.columns:
    print(f"❌ Error: Required column '{required_column}' not found in dataset!")
    print(f"Available columns: {ev_consumption.columns.tolist()}")
    exit()

# ✅ Convert "units" to Numeric
ev_consumption["units"] = pd.to_numeric(ev_consumption["units"], errors="coerce")

# ✅ Remove Negative Values
ev_consumption = ev_consumption[ev_consumption["units"] >= 0]

# ✅ Debugging - Show Basic Stats
print("\n🔹 EV Consumption Data Sample:")
print(ev_consumption[[required_column]].head())

print("\n🔹 Summary Statistics (After Fix):")
print(ev_consumption["units"].describe())

print("\n🔹 Checking for Missing Values:")
print(ev_consumption["units"].isnull().sum())

# ✅ Set Up Visualization
plt.figure(figsize=(10, 6))
sns.histplot(ev_consumption["units"], bins=50, kde=True, color="blue")
plt.xlabel("Units Consumed")
plt.ylabel("Frequency")
plt.title("Distribution of EV Units Consumption (No Negative Values)")
plt.grid(True)

# ✅ Display Plot
plt.show(block=True)
