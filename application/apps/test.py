import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

def app():
    data = pd.read_csv('/Users/richardphilipose/Desktop/final_project/cleaned_va_data.csv')

    st.write("""
    # Atlanta Housing Prediction App
    This app predicts the **Atlanta Housing Prices** !
    """)

    st.sidebar.header('User Input Parameters')

    def user_input_features():
        sepal_length = st.sidebar.slider('# of bedrooms', 4.3, 7.9, 5.4) # first value is minimmum, second value is max and third value is default value
        sepal_width = st.sidebar.slider('Square Feet', 2.0, 4.4, 3.4)
        petal_length = st.sidebar.slider('# of bathrooms', 1.0, 6.9, 1.3)
        petal_width = st.sidebar.slider('Zip Code', 0.1, 2.5, 0.2)
        data = {'sepal_length': sepal_length,
                'sepal_width': sepal_width,
                'petal_length': petal_length,
                'petal_width': petal_width}
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_features()

    st.subheader('User Input parameters')
    st.write(df)

    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    clf = RandomForestClassifier()
    clf.fit(X, Y)

    prediction = clf.predict(df)
    prediction_proba = clf.predict_proba(df)

    st.subheader('Class labels and their corresponding index number')
    st.write(iris.target_names)

    st.subheader('Prediction')
    st.write(iris.target_names[prediction])
    #st.write(prediction)

    st.subheader('Prediction Probability')
    st.write(prediction_proba)