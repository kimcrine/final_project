import streamlit as st
from multiapp import MultiApp
from apps import home, test, va_housing, data, viz

app = MultiApp()

st.markdown("""
This multi-page app is powered by Streamlit
""")

app.add_app("Home", home.app)
app.add_app("Virginia Housing", va_housing.app)
app.add_app("Test", test.app)
app.add_app("Data", data.app)
app.add_app("Visualization", viz.app)

app.run()