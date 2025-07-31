import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path (Update if necessary)
ev_consumption_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/processed_data/ev_consumption_cleaned.csv"

# Load EV Consumption Data
try:
    ev_df = pd.read_csv(ev_consumption_path)
    print("✅ EV Consumption Data Loaded Successfully!\n")
except FileNotFoundError:
    print("❌ Error: The file was not found. Please check the file path.")
    exit()

# Display basic info
print("🔹 Data Overview:")
print(ev_df.info())
print("\n🔹 First 5 Rows:\n", ev_df.head())

# Check for missing values
missing_values = ev_df.isnull().sum()
print("\n🔍 Missing Values:\n", missing_values)

# Fill missing values in 'billdservices' with the mean
if missing_values['billdservices'] > 0:
    ev_df['billdservices'].fillna(ev_df['billdservices'].mean(), inplace=True)
    print("\n✅ Missing values in 'billdservices' filled with column mean.")

# Check for duplicate rows
duplicates = ev_df.duplicated().sum()
print(f"\n🔄 Duplicate Rows Found: {duplicates}")

# Remove duplicates if any
if duplicates > 0:
    ev_df.drop_duplicates(inplace=True)
    print("✅ Duplicates Removed!")

# Summary statistics
print("\n📊 Summary Statistics:\n", ev_df.describe())

# === 📊 VISUALIZATIONS ===

# 1️⃣ Histogram of EV Energy Consumption
plt.figure(figsize=(8, 5))
sns.histplot(ev_df['units'], bins=30, kde=True, color='blue')
plt.xlabel("Units Consumed")
plt.ylabel("Frequency")
plt.title("EV Energy Consumption Distribution")
plt.grid()
plt.show()

# 2️⃣ Bar Plot of Total Services per Area
plt.figure(figsize=(12, 6))
top_areas = ev_df.groupby("area")["totservices"].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_areas.index, y=top_areas.values, palette="viridis")
plt.xticks(rotation=45, ha="right")
plt.xlabel("Area")
plt.ylabel("Total Services")
plt.title("Top 10 Areas with Highest EV Services")
plt.show()

# 3️⃣ Box Plot of Load Distribution
plt.figure(figsize=(8, 5))
sns.boxplot(y=ev_df["load"], color="orange")
plt.ylabel("Load")
plt.title("Load Distribution for EV Charging")
plt.grid()
plt.show()

print("\n🎉 Analysis Completed Successfully!")
