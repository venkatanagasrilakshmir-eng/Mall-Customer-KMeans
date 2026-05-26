from sklearn.cluster import KMeans

def find_optimal_clusters(X):
    wcss = []

    for i in range(1, 11):
        kmeans = KMeans(
            n_clusters=i,
            init='k-means++',
            random_state=42
        )

        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    return wcss

def train_kmeans(X, n_clusters=5):

    kmeans = KMeans(
        n_clusters=n_clusters,
        init='k-means++',
        random_state=42
    )

    y_kmeans = kmeans.fit_predict(X)

    return kmeans, y_kmeans
