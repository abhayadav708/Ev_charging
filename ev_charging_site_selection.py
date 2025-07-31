import pandas as pd

# Load land use data
file_path = "C:\\Users\\prita\\OneDrive\\Desktop\\Ev_charging\\dataset\\geolocation_hyderabad.csv"
land_use_df = pd.read_csv(file_path)

# Define suitable land use types
suitable_land_use = ["TOILETS", "residential", "COMMUNITY HALLS","OPEN SPACES", "PARKS","PLAY GROUNDS","DUMPER BINS",  "HOSPITALS", "ANGANWADI CENTERS","NIGHT SHELTERS","ANNAPURNA MEALS","FIRE STATIONS",   "industrial"]

# Filter the dataset
ev_suitable_df = land_use_df[land_use_df["landuse"].isin(suitable_land_use)]

# Save filtered data
ev_suitable_file = "C:/Users/prita/OneDrive/Desktop/Ev_charging/processed_data/ev_suitable_land_use.csv"
ev_suitable_df.to_csv(ev_suitable_file, index=False)
print("\nEV suitable land use data saved successfully:", ev_suitable_file)

# Display sample locations
print("\nSample EV Charging Site Locations:\n", ev_suitable_df.head())
