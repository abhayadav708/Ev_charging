import pandas as pd

# Load the dataset
file_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\processed_data\ev_consumption_cleaned.csv"
df = pd.read_csv(file_path)

# Summarize EV consumption by area
area_wise_consumption = df.groupby("circle")["units"].sum().reset_index()

# Sort by highest consumption
area_wise_consumption = area_wise_consumption.sort_values(by="units", ascending=False)

# Save the summary
output_path = r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\area_wise_ev_consumption.csv"
area_wise_consumption.to_csv(output_path, index=False)

print(f"✅ Area-wise EV consumption summary saved successfully: {output_path}")
print(area_wise_consumption.head(10))  # Show top 10 areas with highest EV consumption

