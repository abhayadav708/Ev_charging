import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Load the CSV file
csv_file = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\Demographics.csv"
df = pd.read_csv(csv_file)

# Fix column name typo
df.rename(columns={"longitutde": "longitude"}, inplace=True)

# Convert DataFrame to GeoDataFrame
geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# Save as SHP file
shp_file = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\Demographics.shp"
gdf.to_file(shp_file)

print("Shapefile created successfully at:", shp_file)



import geopandas as gpd
shp_file = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\population_density.shp"
gdf = gpd.read_file(shp_file)
print(gdf.head())  # Check first few rows
