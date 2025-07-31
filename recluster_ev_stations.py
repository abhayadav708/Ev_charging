import geopandas as gpd
import numpy as np
from sklearn.cluster import KMeans
from shapely.geometry import Point

# Load original EV stations data
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\clustered_ev_stations\clustered_ev_stations.shp"
ev_stations = gpd.read_file(file_path)

# Extract coordinates
coords = np.array(list(zip(ev_stations.geometry.x, ev_stations.geometry.y)))

# Apply KMeans with optimal k=3
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
ev_stations["new_cluster"] = kmeans.fit_predict(coords)

# Save updated clustered data
output_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\optimized_clusters.shp"
ev_stations.to_file(output_path)

print(f"Re-Clustering Completed. Updated data saved to: {output_path}")
9882551509