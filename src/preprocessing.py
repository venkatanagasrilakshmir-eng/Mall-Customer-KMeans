import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess_data(df):
    X = df.iloc[:, [3, 4]].values
    return X
