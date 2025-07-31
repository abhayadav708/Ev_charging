import geopandas as gpd
import pandas as pd
from sklearn.metrics import silhouette_score

# Load the clustered EV station data
file_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/output/clustered_ev_stations/clustered_ev_stations.shp"
ev_stations = gpd.read_file(file_path)

# Check columns and missing values
print("Columns in dataset:", ev_stations.columns)
print("\nMissing values:\n", ev_stations.isnull().sum())

# Define the features used for clustering
features = ['latitude', 'longitude', 'density']

# Ensure the required columns exist in the dataset
if not all(col in ev_stations.columns for col in features + ['cluster']):
    raise ValueError("Required columns are missing in the dataset!")

# Compute Silhouette Score for existing clusters
silhouette_avg = silhouette_score(ev_stations[features], ev_stations["cluster"])
print("\nSilhouette Score for Current Clusters:", round(silhouette_avg, 4))

# Optimize the number of clusters (example: reduce to 2 clusters if needed)
from sklearn.cluster import KMeans

best_k = 2  # Based on your previous results
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
ev_stations["optimized_cluster"] = kmeans.fit_predict(ev_stations[features])

# Compute Silhouette Score for optimized clusters
optimized_silhouette = silhouette_score(ev_stations[features], ev_stations["optimized_cluster"])
print(f"\nOptimal number of clusters: {best_k} with Silhouette Score: {round(optimized_silhouette, 4)}")

# Fix column name truncation issue for Shapefile format
ev_stations.rename(columns={"optimized_cluster": "opt_cluster"}, inplace=True)

# Save the optimized cluster results
output_file = "C:/Users/prita/OneDrive/Desktop/Ev_charging/output/optimized_ev_stations.shp"
ev_stations.to_file(output_file)

print("\nOptimized cluster data saved successfully:", output_file)



import geopandas as gpd

file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\optimized_ev_stations\optimized_ev_stations.shp"
ev_stations = gpd.read_file(file_path)

print(ev_stations.head())  # Show first few rows
