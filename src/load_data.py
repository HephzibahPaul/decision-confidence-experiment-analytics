import pandas as pd

def load_experiment_data(path="data/experiment_data.csv"):
    return pd.read_csv(path)
