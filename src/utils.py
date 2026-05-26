import pandas as pd

def save_clustered_data(df, y_kmeans):

    df["Cluster"] = y_kmeans

    df.to_csv(
        "outputs/clustered_data.csv",
        index=False
    )
