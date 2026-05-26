import matplotlib.pyplot as plt

def plot_elbow_method(wcss):

    plt.figure(figsize=(8,5))

    plt.plot(range(1,11), wcss, marker='o')

    plt.title("Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")

    plt.savefig("outputs/elbow_method.png")
    plt.close()

def plot_clusters(X, y_kmeans, kmeans):

    plt.figure(figsize=(8,6))

    plt.scatter(
        X[y_kmeans == 0, 0],
        X[y_kmeans == 0, 1],
        s=100,
        label='Cluster 1'
    )

    plt.scatter(
        X[y_kmeans == 1, 0],
        X[y_kmeans == 1, 1],
        s=100,
        label='Cluster 2'
    )

    plt.scatter(
        X[y_kmeans == 2, 0],
        X[y_kmeans == 2, 1],
        s=100,
        label='Cluster 3'
    )

    plt.scatter(
        X[y_kmeans == 3, 0],
        X[y_kmeans == 3, 1],
        s=100,
        label='Cluster 4'
    )

    plt.scatter(
        X[y_kmeans == 4, 0],
        X[y_kmeans == 4, 1],
        s=100,
        label='Cluster 5'
    )

    plt.scatter(
        kmeans.cluster_centers_[:, 0],
        kmeans.cluster_centers_[:, 1],
        s=300,
        c='black',
        marker='X',
        label='Centroids'
    )

    plt.title("Customer Clusters")
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.legend()

    plt.savefig("outputs/customer_clusters.png")
    plt.close()
