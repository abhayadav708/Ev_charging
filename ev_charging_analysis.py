import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the CSV file
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\geolocation_hyderabad.csv"
land_use_df = pd.read_csv(file_path)

# Step 2: Identify relevant column for land use
# Check available columns if needed:
print("Available columns in Land Use Data:\n", land_use_df.columns)

# Step 3: Fill missing values in the 'landuse' column (if any)
if 'landuse' in land_use_df.columns:
    land_use_df['landuse'].fillna('Unknown', inplace=True)
else:
    raise ValueError("Column 'landuse' not found. Check column names!")

# Step 4: Get unique land use types
print("\nUnique Land Use Types:\n", land_use_df['landuse'].unique())

# Step 5: Count the occurrences of each land use type
land_use_counts = land_use_df['landuse'].value_counts()
print("\nLand Use Type Distribution:\n", land_use_counts)

plt.figure(figsize=(10, 6))
sns.barplot(y=land_use_counts.index, x=land_use_counts.values, hue=land_use_counts.index, palette="viridis", legend=False)
plt.xlabel("Count")
plt.ylabel("Land Use Type")
plt.title("Distribution of Land Use Types in Hyderabad")
plt.show()
