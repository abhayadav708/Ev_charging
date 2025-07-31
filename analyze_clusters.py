import geopandas as gpd
import pandas as pd

# Load the optimized clusters shapefile
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\final_optimized_clusters\final_optimized_clusters.shp"

# Read the shapefile
gdf = gpd.read_file(file_path)

# ✅ Rename the truncated 'optimized_' column if needed
if 'optimized_' in gdf.columns:
    gdf.rename(columns={'optimized_': 'optimized_cluster'}, inplace=True)
elif 'opt_cluste' in gdf.columns:
    gdf.rename(columns={'opt_cluste': 'optimized_cluster'}, inplace=True)

# ✅ Correct column names mapping
corrected_columns = {
    'Sex Ratio': 'sex_ratio',  
    'Rural Popu': 'rural_population',  
    'Urban_Popu': 'urban_population'
}
gdf.rename(columns=corrected_columns, inplace=True)

# ✅ Group by the corrected 'optimized_cluster' column
cluster_summary = gdf.groupby("optimized_cluster").agg(
    total_districts=("Districts", "count"),
    avg_population=("density", "mean"),
    avg_sex_ratio=("sex_ratio", "mean"),
    avg_rural_population=("rural_population", "mean"),
    avg_urban_population=("urban_population", "mean")
).reset_index()

# ✅ Save the summary as a CSV
output_csv = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\cluster_analysis.csv"
cluster_summary.to_csv(output_csv, index=False)

print(f"✅ Cluster analysis saved successfully: {output_csv}")
print(cluster_summary)
