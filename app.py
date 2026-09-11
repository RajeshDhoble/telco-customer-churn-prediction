import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("churn_model.pkl")

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Predictor")
st.write("Predict the probability that an existing customer will churn.")

st.divider()

# Customer inputs
contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One Year", "Two Year"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["Yes", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Bank Withdrawal",
        "Credit Card",
        "Mailed Check",
        "Electronic Check"
    ]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No"]
)

unlimited_data = st.selectbox(
    "Unlimited Data",
    ["Yes", "No"]
)

premium_tech_support = st.selectbox(
    "Premium Tech Support",
    ["Yes", "No"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No"]
)

device_protection = st.selectbox(
    "Device Protection Plan",
    ["Yes", "No"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No"]
)

streaming_music = st.selectbox(
    "Streaming Music",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No"]
)

tenure = st.number_input(
    "Tenure in Months",
    min_value=0,
    max_value=100,
    value=12
)

referrals = st.number_input(
    "Number of Referrals",
    min_value=0,
    max_value=100,
    value=0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=500.0
)

monthly_charge = st.number_input(
    "Monthly Charge",
    min_value=0.0,
    value=70.0
)

if st.button("🔮 Predict Churn", use_container_width=True):

    customer = pd.DataFrame([{
        "Contract": contract,
        "Dependents": dependents,
        "Internet Service": internet_service,
        "Payment Method": payment_method,
        "Online Security": online_security,
        "Unlimited Data": unlimited_data,
        "Premium Tech Support": premium_tech_support,
        "Online Backup": online_backup,
        "Device Protection Plan": device_protection,
        "Streaming TV": streaming_tv,
        "Streaming Movies": streaming_movies,
        "Streaming Music": streaming_music,
        "Multiple Lines": multiple_lines,
        "Tenure in Months": tenure,
        "Number of Referrals": referrals,
        "Total Charges": total_charges,
        "Monthly Charge": monthly_charge
    }])

    probability = model.predict_proba(customer)[0, 1]

    st.divider()

    st.subheader("Prediction")

    st.metric(
        "Churn Probability",
        f"{probability:.1%}"
    )

    if probability >= 0.70:
        st.error("🔴 HIGH RISK")
        st.write(
            "Recommended action: Contact the customer and "
            "consider a suitable retention offer."
        )

    elif probability >= 0.40:
        st.warning("🟡 MEDIUM RISK")
        st.write(
            "Recommended action: Monitor the customer and "
            "consider a retention offer."
        )

    else:
        st.success("🟢 LOW RISK")
        st.write(
            "Recommended action: No immediate retention action required."
        )
