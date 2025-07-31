import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/prita/OneDrive/Desktop/Ev_charging/output/ev_station_priority_ranking.csv"
df = pd.read_csv(file_path)

# Set the style for seaborn
sns.set_style("whitegrid")

# Heatmap of Priority Scores
plt.figure(figsize=(8, 5))
sns.heatmap(df.pivot_table(values='Priority_Score', index='optimized_cluster'), cmap="viridis", annot=True, fmt=".2f")
plt.title("Heatmap of Priority Scores by Cluster")
plt.xlabel("Cluster")
plt.ylabel("Priority Score")
plt.savefig("C:/Users/prita/OneDrive/Desktop/Ev_charging/output/heatmap.png")
plt.show()

# Bar Chart for Priority Scores
plt.figure(figsize=(10, 6))
df_sorted = df.sort_values(by="Priority_Score", ascending=False)
sns.barplot(x=df_sorted["optimized_cluster"], y=df_sorted["Priority_Score"], hue=df_sorted["optimized_cluster"], palette="viridis", legend=False)
plt.xlabel("Optimized Cluster")
plt.ylabel("Priority Score")
plt.title("Bar Chart of Priority Scores by Cluster")
plt.xticks(rotation=45)
plt.savefig("C:/Users/prita/OneDrive/Desktop/Ev_charging/output/bar_chart.png")
plt.show()

# Scatter Plot of Clusters vs Priority Score
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["optimized_cluster"], y=df["Priority_Score"], hue=df["optimized_cluster"], palette="viridis", s=100, edgecolor='black')
plt.xlabel("Optimized Cluster")
plt.ylabel("Priority Score")
plt.title("Scatter Plot of Clusters vs Priority Score")
plt.legend(title="Cluster")
plt.savefig("C:/Users/prita/OneDrive/Desktop/Ev_charging/output/scatter_plot.png")
plt.show()

print("✅ Analysis complete. Plots saved successfully!")
