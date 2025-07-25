from omicflow.analysis import run_pca
import pandas as pd
import numpy as np

def test_run_pca():
    df = pd.DataFrame(np.random.rand(10, 5))
    result = run_pca(df)
    assert result.shape == (10, 2)
