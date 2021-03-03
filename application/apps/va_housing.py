import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor

def app():
    dummy_df = pd.read_csv('/Users/richardphilipose/Desktop/final_project/cleaned_va_data.csv')

    st.write("""
    # Virginia House Price Prediction App
    This app predicts the **Virginia House Price**!
    """)
    st.write('---')

    X = dummy_df[['median_pending_sqft',
        'median_days_to_close', 'duration']]

    y = dummy_df['median_sale_price'].values.reshape(-1,1)


    # Sidebar
    # Header of Specify Input Parameters
    st.sidebar.header('Specify Input Parameters')

    def user_input_features():
        median_sqft = st.sidebar.slider('Median Square Feet', 900, 3216, 1912)
        median_days = st.sidebar.slider('Median Days to Close', 0, 62, 28)
        duration = st.sidebar.slider('Duration', 1, 12, 7)
        # location = st.sidebar.selectbox('Location', options )
        
        data = {'Median Square Feet': median_sqft,
                'Median Days to Close': median_days,
                'Duration': duration,
                # 'Location': location
                }
        features = pd.DataFrame(data, index=[0])
        return features

    data = user_input_features()

    # Print specified input parameters
    st.header('Specified Input parameters')
    st.write(data)
    st.write('---')

    # Main Panel


    #encode data

    # encode = ['Location']
    # for col in encode:
    #     dummy = pd.get_dummies(data[col], prefix = col)
    #     data = pd.concat([data, dummy], axis =1)
    #     del data[col]
    # data = data[:1]

    # Build Regression Model
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    from sklearn.preprocessing import StandardScaler
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)

    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Apply Model to Make Prediction
    prediction = model.predict(data)

    st.header('Prediction of Sale Price')
    st.write(prediction)
    st.write('---')

    # # Explaining the model's predictions using SHAP values
    # # https://github.com/slundberg/shap
    # explainer = shap.TreeExplainer(model)
    # shap_values = explainer.shap_values(X)

    # st.header('Feature Importance')
    # plt.title('Feature importance based on SHAP values')
    # shap.summary_plot(shap_values, X)
    # st.pyplot(bbox_inches='tight')
    # st.write('---')

    # plt.title('Feature importance based on SHAP values (Bar)')
    # shap.summary_plot(shap_values, X, plot_type="bar")
    # st.pyplot(bbox_inches='tight')

