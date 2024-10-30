import pandas as pd

FPATH = 'Analytics/loan_data.csv'

def get_data():
    data = pd.read_csv(FPATH)
    return data

def get_purposes():
    data = get_data()
    return data["purpose"].unique()
