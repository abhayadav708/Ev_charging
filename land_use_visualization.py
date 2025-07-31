import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os  # Import os to handle directories

# Load cleaned data
file_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/geolocation_hyderabad.csv"
land_use_df = pd.read_csv(file_path)

# Count land use types
land_use_counts = land_use_df['landuse'].value_counts()

# Ensure the output directory exists
output_dir = "C:/Users/prita/OneDrive/Desktop/Ev_charging/plots"
os.makedirs(output_dir, exist_ok=True)  # ✅ Creates the folder if it doesn't exist

# Plot the distribution
plt.figure(figsize=(10, 6))
sns.barplot(y=land_use_counts.index, x=land_use_counts.values, hue=land_use_counts.index, palette="viridis", legend=False)
plt.xlabel("Count")
plt.ylabel("Land Use Type")
plt.title("Distribution of Land Use Types in Hyderabad")

# Save the figure
output_path = os.path.join(output_dir, "land_use_distribution.png")
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.show()

print("\n✅ Fixed error & saved visualization at:", output_path)
