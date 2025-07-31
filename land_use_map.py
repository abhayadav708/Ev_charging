import pandas as pd
import folium
from folium.plugins import MarkerCluster
import os  

# Load cleaned geolocation data
file_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/geolocation_hyderabad_cleaned.csv"

# Read CSV
land_use_df = pd.read_csv(file_path)

# Define latitude and longitude columns
lat_col, lon_col = 'Latitude', 'Longitude'

# Verify if necessary columns exist
if lat_col not in land_use_df.columns or lon_col not in land_use_df.columns:
    print(f"❌ Error: Columns {lat_col}/{lon_col} not found in CSV. Available columns: {land_use_df.columns}")
    exit()

# Remove rows with missing or invalid coordinates
land_use_df = land_use_df.dropna(subset=[lat_col, lon_col])
land_use_df = land_use_df[(land_use_df[lat_col].apply(lambda x: isinstance(x, (int, float)))) & 
                          (land_use_df[lon_col].apply(lambda x: isinstance(x, (int, float))))]

# Limit data for better performance (adjust the limit if needed)
land_use_df = land_use_df.sample(n=min(5000, len(land_use_df)), random_state=42)

# Create a color mapping for land use categories
unique_land_uses = land_use_df['landuse'].unique()
color_palette = ['blue', 'green', 'red', 'purple', 'orange', 'pink', 'gray', 'cadetblue', 'darkblue', 'darkred']
color_mapping = {category: color_palette[i % len(color_palette)] for i, category in enumerate(unique_land_uses)}

# Initialize the map
hyderabad_map = folium.Map(location=[land_use_df[lat_col].mean(), land_use_df[lon_col].mean()], zoom_start=12)

# Add Marker Cluster for better performance
marker_cluster = MarkerCluster().add_to(hyderabad_map)

# Add markers inside the cluster
for _, row in land_use_df.iterrows():
    land_use_type = row.get('landuse', 'Unknown')
    marker_color = color_mapping.get(land_use_type, 'gray')

    folium.Marker(
        location=[row[lat_col], row[lon_col]],
        popup=f"Land Use: {land_use_type}",
        icon=folium.Icon(color=marker_color)
    ).add_to(marker_cluster)

# Ensure the output directory exists
output_dir = "C:/Users/prita/OneDrive/Desktop/Ev_charging/outputs"
os.makedirs(output_dir, exist_ok=True)

# Save the map
map_file = os.path.join(output_dir, "hyderabad_land_use_map.html")
hyderabad_map.save(map_file)

# Debugging check
if os.path.exists(map_file):
    print(f"\n✅ Interactive map saved successfully at: {map_file}")
else:
    print("\n❌ Error: Map file was not saved. Check directory permissions or try a different location.")
