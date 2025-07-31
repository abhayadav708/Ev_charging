import geopandas as gpd
import matplotlib.pyplot as plt

# Load clustered EV station shapefile
ev_stations = gpd.read_file(r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\clustered_ev_stations\clustered_ev_stations.shp")

# Print first few rows for validation
print(ev_stations.head())

# Check for missing values
print("\nMissing values:\n", ev_stations.isnull().sum())

# Plot EV charging stations on a map
fig, ax = plt.subplots(figsize=(8, 6))
ev_stations.plot(column='cluster', cmap='Set1', legend=True, ax=ax, alpha=0.8)

# Add title
plt.title("EV Charging Station Clusters")
plt.show()
