import pandas as pd
from pyexpat import features
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier

from Analytics.data_loader import get_purposes
from Analytics.analysis import get_data, data_preprocessing
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_selection import SelectKBest, SelectPercentile, chi2

import joblib

# features = ['credit.policy', 'log.annual.inc', 'dti', 'fico', 'delinq.2yrs', 'pub.rec'] # , 'purpose'
# target = 'not.fully.paid'
# # Створення конвеєра з послідовними етапами обробки даних
# pipeline = Pipeline([
#     ('feature_selection', ColumnTransformer([("selector", "passthrough", features)], remainder="drop")),
#     # Вибір кращих ознак
#     ('scaler', StandardScaler()),  # Масштабування даних
#     # ('feature_selection', SelectKBest(k=7)),  # Вибір кращих ознак
#     # ('cat', ),
#     ('classification', RandomForestClassifier(n_estimators=300))  # Класифікація з логістичною регресією
# ])

# def predict_pipeline():
#     data = get_data()
#     # data = data_preprocessing(data)
#
#     X = data[features]
#     y = data[target]
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
#     # Тренування моделі та прогнозування
#     pipeline.fit(X_train, y_train)
#     predictions = pipeline.predict(X_test)
#     return y_test, predictions

def predict_pipeline(fname):
    numeric_features = ['credit.policy', 'log.annual.inc', 'dti', 'fico', 'delinq.2yrs', 'pub.rec']
    numeric_transformer = Pipeline(
        steps=[('scaler', StandardScaler())]
    )

    categorical_features = ['purpose']
    categorical_transformer = Pipeline(
        steps=[
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
            ("selector", SelectPercentile(chi2, percentile=50)),
        ]
    )
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    clf = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(n_estimators=300))
        ]
    )

    features = numeric_features + categorical_features
    target = 'not.fully.paid'

    data = get_data("Analytics/loan_data.csv")
    X = data[features]
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    clf.fit(X_train, y_train)
    print("model score: %.3f" % clf.score(X_test, y_test))
    print(clf.get_params())

    predictions = clf.predict(X_test)
    joblib.dump(clf, fname)

    return y_test, predictions

PIPELINE_F_NAME = 'model.pkl'

def train_pipeline(fname):
    predict_pipeline(fname)
    y_test, predictions = predict_pipeline(PIPELINE_F_NAME)
    analise_prediction(predictions, y_test)

def predict_pipeline_by_val(value_to_predict):
    train_pipeline(PIPELINE_F_NAME)
    pipe = joblib.load(PIPELINE_F_NAME)
    # try:
    #     pipe = joblib.load(PIPELINE_F_NAME)
    # except:
    #     train_pipeline(PIPELINE_F_NAME)
    #     pipe = joblib.load(PIPELINE_F_NAME)

    # apply the whole pipeline to data
    pred = pipe.predict(value_to_predict)
    print(value_to_predict)
    print(pred)
    return pred


def predict(method):
    data = get_data()
    data = data_preprocessing(data)

    X = data.drop("int.rate", axis=1).drop("revol.util", axis=1)
    X = data.drop("inq.last.6mths", axis=1)
    X = data.drop("days.with.cr.line", axis=1)
    X = data.drop("revol.bal", axis=1)
    X = data.drop("installment", axis=1)

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

    y_test, predictions = predict("RandomForestClassifier(n_estimators=300)")
    analise_prediction(predictions, y_test)

    # input_val = {
    #     "credit.policy" : [0],
    #     "purpose" : [get_purposes()[0]],
    #     "int.rate" : [0],
    #     "installment" : [0],
    #     "log.annual.inc" : [0],
    #     "dti" : [0],
    #     "fico" : [0],
    #     # "days." : [0],
    #     # "with.cr.line" : [0],
    #     "revol.bal" : [0],
    #     "revol.util" : [0],
    #     "inq.last.6mths" : [0],
    #     "delinq.2yrs" : [0],
    #     "pub.rec" : [0],
    #     "not.fully.paid" : [0]}
    # vals = input_val.values()
    # df = pd.DataFrame(input_val)
    # # print(df)
    #
    # """
    # purpose_credit_card
    # purpose_debt_consolidation
    # purpose_educational
    # purpose_home_improvement
    # purpose_major_purchase
    # purpose_small_business
    # """
    # print(predict_by_value(df))

    y_test, predictions = predict_pipeline('model.pkl')
    analise_prediction(predictions, y_test)
    # pipe = joblib.load('model.pkl')
    #
    # # New data to predict
    # pr = pd.read_csv('set_to_predict.csv')
    # pred_cols = list(pr.columns.values)[:-1]
    #
    # # apply the whole pipeline to data
    # pred = pd.Series(pipe.predict(pr[pred_cols]))
    # print(pred)
