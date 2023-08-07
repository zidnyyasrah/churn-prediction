import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# Menggunakan joblib untuk meload model

with open('final_pipeline.pkl', 'rb') as file_1:
  pipeline = pickle.load(file_1)

model = load_model('churn_model.h5')

def run():
    # Membuat Title
    st.title('Fill Your Data')
    with st.form('key=form_employee'):

        age = st.number_input('Age',value=25,help='Usia Customer')
        gender = st.radio('Gender', (['M','F']))
        st.markdown('---')

        region_category = st.radio('Region Typees', (['Town','City','Village']))
        membership_category = st.selectbox('Your Membership Category',('No Membership', 'Basic Membership', 'Premium Membership','Silver Membership','Gold Membership','Platinum Membership'))
        preferred_offer_types = st.selectbox('Your Preferred Offer Types',('Gift Vouchers/Coupons', 'Credit/Debit Card Offers', 'Without Offers'))
        joined_through_referral = st.radio('Did you join through referral code?', (['Yes','No']))
        offer_application_preference = st.radio('Offer Application Preference', (['Yes','No']))
        used_special_discount = st.radio('Have you Used Special Discount?', (['Yes','No']))
        past_complaint = st.radio('Have you ever complaint before?', (['Yes','No']))
        complaint_status = st.selectbox('Your Complaint Status',('Not Applicable', 'Unsolved', 'Solved','Solved in Follow-up','No Information Available'))
        
        st.markdown('---')

        medium_of_operation = st.radio('Device type', (['Desktop','Smartphone','Both']))
        internet_option = st.radio('Internet type', (['Wi-Fi','Mobile_Data','Fiber_Optic']))
        days_since_last_login = st.number_input('Days Since Last Login',value=1)
        avg_time_spent = st.number_input('Average Time Spent ', value=25,help='Average time spent by a customer on the website')
        avg_transaction_value = st.number_input('Average Transaction Value ', value=25,help='Average transaction value of a customer')
        avg_frequency_login_days = st.number_input('Average Frequency Login Days ', value=25,help='Number of times a customer has logged in to the website')
        points_in_wallet = st.number_input('Points in Wallet ', value=25,help='Points awarded to a customer on each transaction')
        st.markdown('---')

        year_join = st.number_input('Year Join',value=2015, max_value=2017, min_value=2015)
        month_join = st.number_input('Month',value=1, max_value=12, min_value=1)
        day_join = st.number_input('Year Join',value=1, max_value=30, min_value=1)
        hour_visit = st.number_input('Year Join',value=1, max_value=24, min_value=0)
        minute_visit = st.number_input('Year Join',value=1, max_value=60, min_value=0)
        
        st.markdown('---')
        feedback = st.selectbox('Your Feedback',('No reason specified','Poor Product Quality', 'Too many ads', 'Poor Website','Poor Customer Service',
                                                 'Reasonable Price','User Friendly Website','Products always in Stock','Quality Customer Care'))
        
        submitted = st.form_submit_button('Predict')
    

    # Membuat data inference baru
    data_inf = {
    'age': 22,
    'gender': 'M',
    'region_category': 'City',
    'membership_category': 'Silver Membership',
    'joined_through_referral': 'Yes',
    'preferred_offer_types': 'Without Offers',
    'medium_of_operation': 'Desktop',
    'internet_option': 'Fiber_Optic',
    'days_since_last_login': 5,
    'avg_time_spent': 400,
    'avg_transaction_value': 15000,
    'avg_frequency_login_days': 15,
    'points_in_wallet': 800,
    'used_special_discount': 'Yes',
    'offer_application_preference': 'No',
    'past_complaint': 'No',
    'complaint_status': 'No Information Available',
    'feedback': 'Products always in Stock',
    'year_join': 2017,
    'month_join': 12,
    'day_join': 3,
    'hour_visit': 12,
    'minute_visit': 30,
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    # Predict using ANN
    if submitted:
        # Melakukan prediksi dengan model dari data baru
        data_inf_transform = pipeline.transform(data_inf)
        y_pred_inf = model.predict(data_inf_transform)
        y_pred_inf = np.where(y_pred_inf >= 0.5, 1, 0)
        
        value = ''
        if y_pred_inf == 0:
            value = "You're Likely to stay"
        elif y_pred_inf == 1:
            value = "Positive Churn"
        st.write('# ', value)
        

if __name__ == '__main__':
   run()