import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoJSON file
gdf = gpd.read_file("C:\\Users\\prita\\OneDrive\\Desktop\\Ev_charging\\dataset\\Telangana_Shape_Files\\20231018__Telangana_Shape_Files\\TS_District_Boundary_33\\TS_District_Boundary_33_FINAL_fixed.geojson")

# Plot the district boundaries
gdf.plot(figsize=(10, 8), edgecolor="black", cmap="Set3")
plt.title("Telangana District Boundaries")
plt.show()


import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Load CSV file
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\processed_data\road_network_processed.csv"
df = pd.read_csv(file_path, low_memory=False)  # Avoid dtype warning

# Ensure the dataset has valid Latitude & Longitude
lat_col, lon_col = 'Y', 'X'  # Change these if needed

if lat_col in df.columns and lon_col in df.columns:
    # Convert to GeoDataFrame with geometry column
    df = df.dropna(subset=[lat_col, lon_col])  # Remove rows with missing coordinates
    geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")  # WGS 84 projection

    # Save as Shapefile
    output_shp = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\outputs\road_network.shp"
    gdf.to_file(output_shp, driver='ESRI Shapefile')

    print(f"✅ Successfully converted CSV to SHP: {output_shp}")
else:
    print("❌ Latitude and Longitude columns not found in CSV.")
