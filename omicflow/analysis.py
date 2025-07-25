import pandas as pd
from sklearn.decomposition import PCA

def run_pca(df):
    numeric_df = df.select_dtypes(include='number')
    pca = PCA(n_components=2)
    return pca.fit_transform(numeric_df.dropna())
