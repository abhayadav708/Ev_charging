import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx  # For adding a basemap

# Load clustered EV stations data
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\clustered_ev_stations\clustered_ev_stations.shp"
ev_stations = gpd.read_file(file_path)

# Convert CRS to Web Mercator (EPSG:3857) for accurate map overlay
ev_stations = ev_stations.to_crs(epsg=3857)

# Create plot
fig, ax = plt.subplots(figsize=(10, 8))
ev_stations.plot(column='cluster', cmap='Set1', legend=True, ax=ax, alpha=0.8)

# Add basemap for reference
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

# Title and display
plt.title("EV Charging Station Clusters with Basemap")
plt.show()
