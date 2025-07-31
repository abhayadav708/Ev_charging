import pandas as pd

# Load the cleaned dataset
file_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/output/ev_consumption_cluster_analysis_final.csv"
df = pd.read_csv(file_path)

# Fill missing values with 0
df.fillna(0, inplace=True)

# Compute Priority Score for each cluster
df["Priority_Score"] = (
    (df["units"] * 0.4) + 
    (df["avg_urban_population"] * 0.3) + 
    (df["load"] * 0.2) - 
    (df["totservices"] * 0.1)
)

# Sort clusters by highest priority for EV stations
df_sorted = df.sort_values(by="Priority_Score", ascending=False)

# Save the ranked locations
output_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/output/ev_station_priority_ranking.csv"
df_sorted.to_csv(output_path, index=False)

# Show top 10 locations for EV charging stations
print("✅ Top 10 Locations for EV Charging Stations:")
print(df_sorted[["optimized_cluster", "Priority_Score"]].head(10))
print(f"📂 Ranked list saved at: {output_path}")
