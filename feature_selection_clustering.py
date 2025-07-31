import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
file_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/Demographics.csv"
df = pd.read_csv(file_path)

# Select relevant features for clustering
selected_features = ["latitude", "longitude", "density", "Rural Population (%)", "Urban Population (%)"]
df = df[selected_features].copy()

# Handle missing values (optional: remove or fill)
df.dropna(inplace=True)  # Remove rows with missing values

# Normalize Population Density and Population Percentages
scaler = MinMaxScaler()
df[["density", "Rural Population (%)", "Urban Population (%)"]] = scaler.fit_transform(df[["density", "Rural Population (%)", "Urban Population (%)"]])

# Save processed data for clustering
processed_file_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/processed_data/demographics_processed.csv"
df.to_csv(processed_file_path, index=False)

print(f"Processed data saved at: {processed_file_path}")
