import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from shapely.geometry import Point

# Load the demographics dataset
demographics_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\Demographics\Demographics.shp"
demographics = gpd.read_file(demographics_path)

# Rename columns to standard format if necessary
demographics = demographics.rename(columns={'Urban Popu': 'Urban_Population'})

# Select relevant features for clustering
features = demographics[['latitude', 'longitude', 'density', 'Urban_Population']].dropna()

# Number of clusters (adjust based on your requirement)
num_clusters = 5

# Apply K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
features['cluster'] = kmeans.fit_predict(features[['latitude', 'longitude', 'density', 'Urban_Population']])

# Add cluster labels to the original dataset
demographics['cluster'] = features['cluster']

# Load additional datasets (Land Use & Road Network)
land_use_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\land_use\landuse.shp"
road_network_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\road_network\road_network.shp"

land_use = gpd.read_file(land_use_path)
road_network = gpd.read_file(road_network_path)

# Plot the clustering results
fig, ax = plt.subplots(figsize=(10, 8))
demographics.plot(column='cluster', cmap='Set1', legend=True, alpha=0.6, ax=ax)
land_use.plot(color='green', alpha=0.3, ax=ax)
road_network.plot(color='black', linewidth=0.5, ax=ax)

plt.title("EV Charging Station Clustering")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Save clustered results
output_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\clustered_ev_stations.shp"
demographics.to_file(output_path)

print(f"Clustering complete. Results saved at: {output_path}")
