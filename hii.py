import geopandas as gpd

# ✅ Correct shapefile path
shapefile_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\dataset\Telangana_Shape_Files\20231018__Telangana_Shape_Files\TS_District_Boundary_33\TS_District_Boundary_33_FINAL.shp"

# ✅ Define GeoJSON output path
output_geojson = shapefile_path.replace(".shp", "_fixed.geojson")

try:
    print("🔄 Loading shapefile...")
    districts_gdf = gpd.read_file(shapefile_path)

    # ✅ Check if the file loaded correctly
    if districts_gdf.empty:
        raise ValueError("Shapefile loaded but is empty! Check file integrity.")

    print(f"📌 Original CRS: {districts_gdf.crs}")

    # ✅ Convert to EPSG:4326 (WGS 84) instead of forcing a new CRS
    if districts_gdf.crs is None:
        print("⚠️ CRS is missing. Assigning EPSG:4326.")
        districts_gdf.set_crs(epsg=4326, inplace=True, allow_override=True)
    else:
        print(f"🔄 Transforming CRS to EPSG:4326...")
        districts_gdf = districts_gdf.to_crs(epsg=4326)

    print("✅ CRS successfully converted!")

    # ✅ Save as GeoJSON
    districts_gdf.to_file(output_geojson, driver="GeoJSON")
    print(f"✅ GeoJSON saved successfully at: {output_geojson}")

except FileNotFoundError:
    print("❌ Error: The specified shapefile path does not exist.")
except ValueError as ve:
    print(f"❌ Data Error: {ve}")
except Exception as e:
    print(f"❌ Unexpected Error: {e}")



