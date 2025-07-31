import pandas as pd

# Load datasets
ev_file = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\processed_data\ev_consumption_cleaned.csv"
cluster_file = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\cluster_analysis.csv"

ev_df = pd.read_csv(ev_file)
cluster_df = pd.read_csv(cluster_file)

# Check if the 'area' in EV data matches any cluster's geographical details (manual mapping needed if not)
# Assuming 'optimized_cluster' is our common key

# Step 1: Aggregate EV data by 'area'
ev_summary = ev_df.groupby("area").agg({
    "units": "sum",
    "load": "mean",
    "totservices": "sum",
    "billdservices": "sum"
}).reset_index()

# Step 2: Manually map 'area' to 'optimized_cluster' (since no direct mapping is available)
# This part needs manual intervention if automatic mapping fails
area_to_cluster = {
    "SANATHNAGAR": 1,  # Example: Mapping area names to cluster numbers
    "ERRAGADDA": 1,
    "NEW ERRAGADDA": 1,
    "SOME OTHER AREA": 0  # Add more mappings as needed
}

# Assign clusters based on mapping
ev_summary["optimized_cluster"] = ev_summary["area"].map(area_to_cluster)

# Step 3: Merge EV data with cluster data
final_ev_cluster = ev_summary.groupby("optimized_cluster").agg({
    "units": "sum",
    "load": "mean",
    "totservices": "sum",
    "billdservices": "sum"
}).reset_index()

# Merge with Cluster Analysis dataset
final_cluster_analysis = cluster_df.merge(final_ev_cluster, on="optimized_cluster", how="left")

# Save the final output
output_file = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\ev_consumption_cluster_analysis_final.csv"
final_cluster_analysis.to_csv(output_file, index=False)

print(f"✅ EV Consumption Integration Completed! Data saved at {output_file}")




