import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='Customer Churn Prediction - EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat Title
    st.title('Customer Churn Prediction')

    # Streamlit sub header
    st.subheader('EDA untuk Customer Churn Prediction')


    # Menambahkan Deskripsi
    st.write('Page ini dibuat oleh _Zidny Yasrah Sallum_')
    st.write('## Dataframe Quick Peek')

    # Show DataFrame
    data = pd.read_csv('https://raw.githubusercontent.com/zidnyyasrah/churn-prediction/main/churn.csv')
    st.dataframe(data)
    st.markdown('---')


    # Membuat plotly plot
    st.write('#### Plotly Plot - Feedback | Age')
    fig = px.bar(data, x='feedback', y='age', hover_data=['churn_risk_score'])
    st.plotly_chart(fig)


    # Membuat Histogram Berdasarkan Input User
    st.write('#### Histogram on Various Features')
    choice = st.radio('Select Columns : ', ('days_since_last_login','avg_time_spent','avg_transaction_value','avg_frequency_login_days','points_in_wallet'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[choice], bins=30, kde=True)
    st.pyplot(fig)


if __name__ == '__main__':
    run()