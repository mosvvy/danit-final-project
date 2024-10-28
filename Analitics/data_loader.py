import pandas as pd

FPATH = 'loan_data.csv'

def get_data():
    data = pd.read_csv(FPATH)
    return data
