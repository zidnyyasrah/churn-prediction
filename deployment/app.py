import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Pilih Halaman: ', ('EDA', 'Predict'))

if navigation == 'EDA':
    eda.run()
elif navigation == 'Predict':
    prediction.run()