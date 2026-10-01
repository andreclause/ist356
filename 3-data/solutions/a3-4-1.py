import streamlit as st
import pandas as pd


#main
checks = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv')

checks['total_cleaned'] = checks['total amount of check'].apply(clean_currency)
checks['gratuity_cleaned'] = checks.apply(
    lambda row: clean_currency(row['gratuity']), axis=1
)

x=10
y = lambda x: x +10
def y(x):
    return x + 10

st.dataframe(checks)
