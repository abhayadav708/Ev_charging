import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import contextily as ctx

# Load the dataset
file_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/Demographics.csv"
df = pd.read_csv(file_path)

# Select relevant features for clustering
features = ["density", "Urban Population (%)", "latitude", "longitude"]
df_selected = df[features].dropna()  # Remove rows with missing values

# Normalize the data
scaler = StandardScaler()
df_selected_scaled = scaler.fit_transform(df_selected[["density", "Urban Population (%)"]])

# Determine optimal clusters using the Elbow Method (optional)
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(df_selected_scaled)
    wcss.append(kmeans.inertia_)

# Plot Elbow Method (optional step)
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='-')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method for Optimal k')
plt.show()

# Apply K-Means with chosen number of clusters (e.g., k=4)
optimal_k = 4  # Adjust this based on the elbow plot
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df_selected["Cluster"] = kmeans.fit_predict(df_selected_scaled)

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(df_selected, geometry=gpd.points_from_xy(df_selected["longitude"], df_selected["latitude"]), crs="EPSG:4326")

# Plot Clusters
fig, ax = plt.subplots(figsize=(10, 8))
gdf.plot(column="Cluster", cmap="viridis", legend=True, markersize=50, ax=ax)
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
ax.set_title("K-Means Clustering of EV Charging Stations")
plt.show()

# Save clustered data to a new file
output_file = "C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/clustered_demographics.csv"
gdf.to_csv(output_file, index=False)
print(f"Clustered data saved to {output_file}")
