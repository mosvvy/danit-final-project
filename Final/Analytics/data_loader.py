import pandas as pd

FPATH = 'loan_data.csv'

def get_data(file_path=FPATH):
    data = pd.read_csv(file_path)
    return data

def get_purposes():
    data = get_data()
    return data["purpose"].unique()
