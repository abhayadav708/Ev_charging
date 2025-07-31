import geopandas as gpd
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 1: Load the dataset
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\optimized_ev_stations\optimized_ev_stations.shp"
output_file = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\final_optimized_clusters\final_optimized_clusters.shp"

gdf = gpd.read_file(file_path)

# Step 2: Select relevant features for clustering
features = ['latitude', 'longitude', 'density']  # Modify based on your data

X = gdf[features]

# Step 3: Determine optimal number of clusters (using Silhouette Score)
best_k = 2  # Assuming 2 is optimal based on previous tests
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
gdf['optimized_cluster'] = kmeans.fit_predict(X)

# Step 4: Calculate the silhouette score for evaluation
silhouette_avg = silhouette_score(X, gdf['optimized_cluster'])
print(f"Optimal number of clusters: {best_k} with Silhouette Score: {silhouette_avg}")

# Step 5: Save the updated GeoDataFrame as a Shapefile
gdf.to_file(output_file)

print(f"Optimized clusters saved successfully: {output_file}")
