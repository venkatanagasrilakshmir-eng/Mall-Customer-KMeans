from src.preprocessing import load_data, preprocess_data
from src.train_model import find_optimal_clusters, train_kmeans
from src.visualize import plot_elbow_method, plot_clusters
from src.utils import save_clustered_data

# Load Dataset
df = load_data("dataset/Mall_Customers.csv")

# Preprocess
X = preprocess_data(df)

# Elbow Method
wcss = find_optimal_clusters(X)

# Plot Elbow Graph
plot_elbow_method(wcss)

# Train Model
kmeans, y_kmeans = train_kmeans(X, n_clusters=5)

# Plot Clusters
plot_clusters(X, y_kmeans, kmeans)

# Save Output
save_clustered_data(df, y_kmeans)

print("K-Means Customer Segmentation Completed!")
