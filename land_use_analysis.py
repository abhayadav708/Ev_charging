import pandas as pd

# Load the land use dataset
file_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/geolocation_hyderabad.csv"
land_use_df = pd.read_csv(file_path)

# Fix the warning by using assignment instead of inplace=True
if 'landuse' in land_use_df.columns:
    land_use_df['landuse'] = land_use_df['landuse'].fillna('Unknown')

# Display unique land use types
print("\nUnique Land Use Types:\n", land_use_df['landuse'].unique())

# Save the cleaned data again
cleaned_file = "C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/geolocation_hyderabad_cleaned.csv"
land_use_df.to_csv(cleaned_file, index=False)
print("\n✅ Fixed warning & saved cleaned land use data at:", cleaned_file)
