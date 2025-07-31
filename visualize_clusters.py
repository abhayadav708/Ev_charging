import geopandas as gpd
import folium

# Load the optimized clusters shapefile
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\final_optimized_clusters\final_optimized_clusters.shp"

# Read the shapefile
gdf = gpd.read_file(file_path)

# ✅ Check available columns (to confirm column name truncation)
print("Columns in dataset:", gdf.columns)

# ✅ Rename the truncated column if needed
if 'optimized_' in gdf.columns:
    gdf.rename(columns={'optimized_': 'optimized_cluster'}, inplace=True)

# Create a Folium map centered on Hyderabad
m = folium.Map(location=[17.3850, 78.4867], zoom_start=8)

# Add cluster points to the map
for _, row in gdf.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=f"Cluster: {row.optimized_cluster}",
        icon=folium.Icon(color="blue" if row.optimized_cluster == 0 else "red")
    ).add_to(m)

# Save the map
map_output = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\outputs\cluster_map.html"
m.save(map_output)

print(f"✅ Map saved successfully: {map_output}")






import pandas as pd

# Define file path
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\processed_data\ev_consumption_cleaned.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Display the first few rows
print(df.head())

# Show column names for reference
print("\nColumns in the dataset:", df.columns)

