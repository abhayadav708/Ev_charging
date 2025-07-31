import pandas as pd

# Load your dataset
file_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/output/ev_consumption_cluster_analysis_final.csv"
df = pd.read_csv(file_path)

# Fill missing values with 0
df.fillna(0, inplace=True)

# Save the cleaned dataset
df.to_csv(file_path, index=False)

print("✅ Missing values handled successfully!")
