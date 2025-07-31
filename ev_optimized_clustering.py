import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx
from sklearn.cluster import KMeans

# ✅ Define File Paths
demographics_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\Demographics\Demographics.shp"
land_use_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\land_use\landuse.shp"
road_network_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\road_network\road_network.shp"

# ✅ Load Geospatial Data
demographics = gpd.read_file(demographics_path)
land_use = gpd.read_file(land_use_path)
road_network = gpd.read_file(road_network_path)

# ✅ Convert CRS to EPSG:3857 for Uniform Projection
demographics = demographics.to_crs(epsg=3857)
land_use = land_use.to_crs(epsg=3857)
road_network = road_network.to_crs(epsg=3857)

# ✅ Select Features for Clustering (Latitude, Longitude, Density)
features = demographics[['latitude', 'longitude', 'density']]

# ✅ Perform K-Means Clustering (Adjust K as Needed)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
demographics['cluster'] = kmeans.fit_predict(features)

# ✅ Plot the Clusters on a Map
fig, ax = plt.subplots(figsize=(10, 8))
demographics.plot(column='cluster', cmap='rainbow', alpha=0.7, legend=True, ax=ax)

# ✅ Overlay Land Use and Road Network Data
land_use.plot(column='type', cmap='Set3', alpha=0.5, legend=True, ax=ax)
road_network.plot(color="black", linewidth=0.5, ax=ax)

# ✅ Add Basemap for Better Visualization
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

# ✅ Save and Show the Clustered Map
ax.set_title("Optimized EV Charging Station Clustering with Land Use & Road Network")
plt.savefig("ev_cluster_analysis.png")
plt.show()

print("✅ Clustering completed! Check 'ev_cluster_analysis.png' for results.")
