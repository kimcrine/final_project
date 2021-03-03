import streamlit as st
import pandas as pd

def app():

    data = pd.read_csv('/Users/richardphilipose/Desktop/final_project/cleaned_va_data.csv')

    st.write("""
    # Virginia House Price Data
    """)
    st.write('---')

    st.write(data)
    st.line_chart(data)

