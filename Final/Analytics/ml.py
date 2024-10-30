import pandas as pd

from analysis import get_data, data_preprocessing
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

from data_loader import get_purposes


def predict(method):
    data = get_data()
    data = data_preprocessing(data)

    X = data.drop("not.fully.paid", axis=1)
    y = data["not.fully.paid"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    dtree = eval(method)
    dtree.fit(X_train, y_train)

    predictions = dtree.predict(X_test)
    return y_test, predictions

def analise_prediction(predictions, y_test):
    print(classification_report(y_test, predictions))
    print(confusion_matrix(y_test, predictions))

    # df_pred=pd.DataFrame(predictions)
    # plt.figure(figsize=(15, 10))
    # sns.countplot(predictions)
    # plt.show()

def predict_by_value(value_to_predict):
    data = get_data()
    # print(data.shape)
    data = data._append(value_to_predict, ignore_index=True)
    # print(data.shape)
    data = data_preprocessing(data)

    X = data.drop("not.fully.paid", axis=1)[:-1]
    # print(X.shape)
    y = data["not.fully.paid"][:-1]
    p = data.drop("not.fully.paid", axis=1).tail(1)
    # print(type(p))
    # print(p)

    df = RandomForestClassifier()
    df.fit(X, y)

    prediction = df.predict(p)
    return prediction



if __name__ == '__main__':

    # y_test, predictions = predict("DecisionTreeClassifier()")
    # analise_prediction(predictions, y_test)
    #
    # y_test, predictions = predict("RandomForestClassifier(n_estimators=300)")
    # analise_prediction(predictions, y_test)

    input_val = {
        "credit.policy" : [0],
        "purpose" : [get_purposes()[0]],
        "int.rate" : [0],
        "installment" : [0],
        "log.annual.inc" : [0],
        "dti" : [0],
        "fico" : [0],
        # "days." : [0],
        # "with.cr.line" : [0],
        "revol.bal" : [0],
        "revol.util" : [0],
        "inq.last.6mths" : [0],
        "delinq.2yrs" : [0],
        "pub.rec" : [0],
        "not.fully.paid" : [0]}
    vals = input_val.values()
    df = pd.DataFrame(input_val)
    # print(df)

    """
    purpose_credit_card       
    purpose_debt_consolidation
    purpose_educational       
    purpose_home_improvement  
    purpose_major_purchase    
    purpose_small_business    
    """
    print(predict_by_value(df))
