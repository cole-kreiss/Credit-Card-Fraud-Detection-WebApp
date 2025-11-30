import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Credit_Card_Fraud_Detection_Pipeline.pkl")

st.title("Credit Card Fraud Detection App")

st.markdown("Please enter credit card transaction details and click the Predict button")

st.divider()

repeat_retailer = st.selectbox("Repeat Retailer", {1.0, 0.0})
used_chip = st.selectbox("Used EMV Chip", {1.0, 0.0})
used_pin = st.selectbox("Used Pin Number", {1.0, 0.0})
online_order = st.selectbox("Online Order", {1.0, 0.0})
distance_from_home = st.number_input("Distance in miles from home address", min_value=0.0, max_value=12500.0, value=5.0)
distance_from_last_transaction = st.number_input("Distance in miles from last transaction", min_value=0.0, max_value=12500.0, value=5.0)
purchase_price_ratio_to_median = st.number_input("Ratio of purchase price compared to median price", min_value=0.0, value=1.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{

        "distance_from_home" : distance_from_home,
        "distance_from_last_transaction" : distance_from_last_transaction,
        "ratio_to_median_purchase_price" : purchase_price_ratio_to_median,
        "repeat_retailer" : repeat_retailer,
        "used_chip" : used_chip,
        "used_pin_number" : used_pin,
        "online_order" : online_order

    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction == 1:
        st.error("This credit card transaction is likely fraud!")
    else:
        st.success("This credit card transaction is likely legitimate.")