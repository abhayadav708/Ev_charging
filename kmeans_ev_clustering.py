import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load Demographics Data
csv_file = "C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/Demographics.csv"
df = pd.read_csv(csv_file)

# Feature Selection: Using relevant columns for clustering
features = ["density", "Urban Population (%)", "latitude", "longitude"]
df_selected = df[features].dropna()

# Normalize the data for better clustering
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_selected[["density", "Urban Population (%)"]])

# Finding the optimal number of clusters using the Elbow Method
wcss = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Method Graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, 10), wcss, marker='o', linestyle='-')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("WCSS")
plt.title("Elbow Method for Optimal k")
plt.show()

# Choose the optimal k from the elbow method (let's assume k=4 for now)
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df_selected["Cluster"] = kmeans.fit_predict(df_scaled)

# Add cluster labels to the original dataframe
df["Cluster"] = df_selected["Cluster"]

# Save the clustered data
output_csv = "C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/clustered_demographics.csv"
df.to_csv(output_csv, index=False)
print(f"Clustered data saved to: {output_csv}")

# Convert DataFrame to GeoDataFrame for visualization
gdf = gpd.GeoDataFrame(df_selected, geometry=gpd.points_from_xy(df_selected["longitude"], df_selected["latitude"]))
gdf.set_crs(epsg=4326, inplace=True)  # Set CRS

# Plot Clusters on a Map
fig, ax = plt.subplots(figsize=(10, 8))
gdf.plot(column="Cluster", cmap="Set1", legend=True, markersize=50, ax=ax)
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
ax.set_title("EV Charging Station Clustering")
plt.savefig("C:/Users/prita/OneDrive/Desktop/Ev_charging/output/ev_clusters.png")
plt.show()

print("Clustering and visualization completed!")

