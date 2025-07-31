import geopandas as gpd
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

# Load clustered EV stations data
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\clustered_ev_stations\clustered_ev_stations.shp"
ev_stations = gpd.read_file(file_path)

# Extract latitude, longitude, and cluster labels
coords = np.array(list(zip(ev_stations.geometry.x, ev_stations.geometry.y)))
cluster_labels = ev_stations["cluster"]

# Compute Silhouette Score (measures clustering quality)
sil_score = silhouette_score(coords, cluster_labels)
print(f"Silhouette Score: {sil_score:.4f}")

# Optional: Evaluate cluster balance (count of points per cluster)
cluster_counts = ev_stations["cluster"].value_counts()
print("\nCluster Distribution:\n", cluster_counts)

# Re-cluster with optimized K (if needed)
if sil_score < 0.5:  # Threshold can be adjusted
    optimal_k = range(2, 10)  # Testing different cluster sizes
    best_score = -1
    best_k = None

    for k in optimal_k:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        new_labels = kmeans.fit_predict(coords)
        score = silhouette_score(coords, new_labels)

        if score > best_score:
            best_score = score
            best_k = k

    print(f"\nOptimal number of clusters: {best_k} with Silhouette Score: {best_score:.4f}")
