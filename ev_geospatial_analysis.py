import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx
import os

# Define file paths
population_shp = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\Demographics\Demographics.shp"
land_use_shp = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\land_use\landuse.shp"
road_network_shp = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\road_network\road_network.shp"

# Check if shapefiles exist
for file in [population_shp, land_use_shp ]:
    if not os.path.exists(file):
        print(f"Error: File not found - {file}")
        exit()

# Load Geospatial Data
population_data = gpd.read_file(population_shp)
land_use_data = gpd.read_file(land_use_shp)
road_network_data = gpd.read_file(road_network_shp)

# Convert CRS to a common projection (Web Mercator - EPSG:3857)
population_data = population_data.to_crs(epsg=3857)
land_use_data = land_use_data.to_crs(epsg=3857)
road_network_data = road_network_data.to_crs(epsg=3857)

# Normalize population density values (if 'density' column exists)
if "density" in population_data.columns:
    population_data["norm_density"] = (
        (population_data["density"] - population_data["density"].min()) /
        (population_data["density"].max() - population_data["density"].min())
    )
else:
    print("Error: 'density' column not found in Demographics.shp")
    exit()

# Create output directory if it doesn't exist
output_dir = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output"
os.makedirs(output_dir, exist_ok=True)

# Plot Population Density Heatmap
fig, ax = plt.subplots(figsize=(10, 8))
population_data.plot(column="norm_density", cmap="Reds", alpha=0.6, legend=True, ax=ax)
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
ax.set_title("Population Density Heatmap")
plt.savefig(os.path.join(output_dir, "population_density_heatmap.png"))
plt.show()

# Plot Road Network
fig, ax = plt.subplots(figsize=(10, 8))
road_network_data.plot(color="black", linewidth=0.5, ax=ax)
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
ax.set_title("Road Network Map")
plt.savefig(os.path.join(output_dir, "road_network.png"))
plt.show()

# Plot Land Use Distribution
fig, ax = plt.subplots(figsize=(10, 8))
land_use_data.plot(column="landuse", cmap="Set3", legend=True, ax=ax)
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
ax.set_title("Land Use Classification")
plt.savefig(os.path.join(output_dir, "land_use.png"))
plt.show()

print("✅ Geospatial Analysis Completed: Heatmaps and Road Networks Saved.")



