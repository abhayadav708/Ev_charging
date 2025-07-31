import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon

# Define the path to your CSV file
csv_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\road_network.csv"

# Load the CSV file
df = pd.read_csv(csv_path, low_memory=False)

# Function to parse the geometry string into a Shapely Polygon
def parse_geometry(geom_str):
    try:
        # Remove extra brackets and split into coordinate pairs
        geom_str = geom_str.strip('[]')
        coords = [list(map(float, pair.split(','))) for pair in geom_str.split('], [')]
        
        # Ensure the polygon has at least 4 coordinates
        if len(coords) >= 4:
            return Polygon(coords)
        else:
            return None  # Skip invalid geometries
    except Exception as e:
        print(f"Error parsing geometry: {e}")
        return None  # Skip rows with invalid geometry

# Apply the function to the geometry column
df['geometry'] = df['geometry'].apply(parse_geometry)

# Drop rows with invalid geometry
df = df.dropna(subset=['geometry'])

# Convert the DataFrame to a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='geometry')

# Set the coordinate reference system (CRS) to WGS84 (EPSG:4326)
gdf.set_crs(epsg=4326, inplace=True)

# Define the output Shapefile path
output_shp_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\road_network.shp"

# Save the GeoDataFrame as a Shapefile
gdf.to_file(output_shp_path)

print(f"Shapefile saved to: {output_shp_path}")