from Analytics.data_loader import get_data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def data_preprocessing(data):
    # print(data.describe(include='all').transpose())

    data_numeric = data.copy()

    for col in data_numeric:
        if col == 'purpose':
            data_numeric = pd.get_dummies(data_numeric,columns=[col],drop_first=True)
        else:
            # try sklearn.preprocessing.MinMaxScaler
            data_numeric[col] = (data_numeric[col] - data_numeric[col].min()) / (data_numeric[col].max() - data_numeric[col].min())

    # print(data_numeric.describe(include='all').transpose())
    return data_numeric

def data_corr(data):
    corr = data.corr(numeric_only=True)
    sns.heatmap(corr, annot=True)
    plt.show()

if __name__ == '__main__':
    data = get_data()
    data = data_preprocessing(data)

    # print(data.info())

    sns.jointplot(x="fico", y="credit.policy", data=data, hue="not.fully.paid", space=0.2)
    plt.show()


    data_corr(data)
