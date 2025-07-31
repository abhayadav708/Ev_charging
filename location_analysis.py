import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the correct file path
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\processed_data\ev_consumption_processed.csv"  # Change filename if needed

# Load dataset
df = pd.read_csv(file_path)

# Group by location and compute total & average energy consumption
location_consumption = df.groupby("circle")["units"].agg(["sum", "mean"]).reset_index()
location_consumption.columns = ["circle", "total_units", "avg_units"]

# Sort by total energy consumption and take the top 10 locations
top_10_locations = location_consumption.sort_values(by="total_units", ascending=False).head(10)

# Plot bar chart
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_10_locations,
    x="total_units",
    y="circle",
    hue="circle",  # Assigning hue to y-variable
    palette="viridis",
    legend=False  # Hides legend
)
plt.xlabel("Total Units Consumed", fontsize=12)
plt.ylabel("Location", fontsize=12)
plt.title("Top 10 Locations with Highest EV Energy Consumption", fontsize=14)
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.show()
