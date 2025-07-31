import geopandas as gpd
import matplotlib.pyplot as plt

# Load datasets
ev_stations = gpd.read_file(r"C:\Users\prita\OneDrive\Desktop\Ev_charging\output\clustered_ev_stations\clustered_ev_stations.shp")
road_network = gpd.read_file("C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/road_network/road_network.shp")
land_use = gpd.read_file("C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/land_use/landuse.shp")
demographics = gpd.read_file("C:/Users/prita/OneDrive/Desktop/Ev_charging/dataset/Demographics/Demographics.shp")

# Ensure all datasets are in the same coordinate reference system (CRS)
ev_stations = ev_stations.to_crs(road_network.crs)
land_use = land_use.to_crs(road_network.crs)
demographics = demographics.to_crs(road_network.crs)

# Create a validation plot
fig, ax = plt.subplots(figsize=(10, 8))
land_use.plot(column="type", cmap="Set3", alpha=0.5, legend=True, ax=ax)  # Land use layer
road_network.plot(color="black", linewidth=0.8, ax=ax)  # Road network layer
demographics.plot(column="density", cmap="OrRd", alpha=0.6, ax=ax)  # Population density
ev_stations.plot(color="red", markersize=50, edgecolor="black", ax=ax)  # EV stations

# Titles and legends
plt.title("EV Charging Station Validation")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(["Roads", "EV Stations", "Population Density", "Land Use"])

# Save the validation plot
plt.savefig("C:/Users/prita/OneDrive/Desktop/Ev_charging/output/validation_plot.png", dpi=300)

plt.show()

# Check if EV stations are within Hyderabad boundaries
hyderabad_boundary = demographics.unary_union  # Assuming demographics represent Hyderabad boundary
out_of_bounds = ev_stations[~ev_stations.within(hyderabad_boundary)]

if not out_of_bounds.empty:
    print("Warning: Some EV stations are outside Hyderabad boundaries!")
else:
    print("✅ All EV stations are within Hyderabad.")

# Check proximity to roads (buffer of 500m)
ev_stations["near_road"] = ev_stations.geometry.apply(lambda x: road_network.distance(x).min() < 500)

if ev_stations["near_road"].sum() < len(ev_stations) * 0.8:
    print("⚠️ Some EV stations are not close to major roads!")
else:
    print("✅ Most EV stations are near major roads.")

# Save the validated dataset
ev_stations.to_file("C:/Users/prita/OneDrive/Desktop/Ev_charging/output/validated_ev_stations.shp")
print("✅ Validation complete. Results saved as 'validated_ev_stations.shp' and 'validation_plot.png'.")



