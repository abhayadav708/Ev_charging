import geopandas as gpd
import folium

# Load the optimized clusters shapefile
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\final_optimized_clusters\final_optimized_clusters.shp"
gdf = gpd.read_file(file_path)

# ✅ Rename the truncated 'optimized_' column if needed
if 'optimized_' in gdf.columns:
    gdf.rename(columns={'optimized_': 'optimized_cluster'}, inplace=True)
elif 'opt_cluste' in gdf.columns:
    gdf.rename(columns={'opt_cluste': 'optimized_cluster'}, inplace=True)

# ✅ Define Map Center
map_center = [gdf["latitude"].mean(), gdf["longitude"].mean()]
ev_map = folium.Map(location=map_center, zoom_start=10)

# ✅ Define Cluster Colors
colors = ['red', 'blue', 'green', 'purple', 'orange']
gdf['color'] = gdf['optimized_cluster'].apply(lambda x: colors[int(x) % len(colors)])

# ✅ Add Markers
for _, row in gdf.iterrows():
    folium.Marker(
        location=[row.latitude, row.longitude],
        popup=f"Cluster: {row.optimized_cluster}",
        icon=folium.Icon(color=row.color)
    ).add_to(ev_map)

# ✅ Save the map as an HTML file
output_map = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\outputs\ev_cluster_map.html"
ev_map.save(output_map)

print(f"✅ EV Cluster Map saved successfully: {output_map}")
