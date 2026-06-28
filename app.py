import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("phishing_model.pkl")

st.title("🔐 Phishing Website Detection System")
st.write("Enter feature values (-1, 0, 1) and get prediction")

# Feature names from your dataset (IMPORTANT: order must match training)
features = [
    "having_IPhaving_IP_Address",
    "URLURL_Length",
    "Shortining_Service",
    "having_At_Symbol",
    "double_slash_redirecting",
    "Prefix_Suffix",
    "having_Sub_Domain",
    "SSLfinal_State",
    "Domain_registeration_length",
    "Favicon",
    "port",
    "HTTPS_token",
    "Request_URL",
    "URL_of_Anchor",
    "Links_in_tags",
    "SFH",
    "Submitting_to_email",
    "Abnormal_URL",
    "Redirect",
    "on_mouseover",
    "RightClick",
    "popUpWidnow",
    "Iframe",
    "age_of_domain",
    "DNSRecord",
    "web_traffic",
    "Page_Rank",
    "Google_Index",
    "Links_pointing_to_page",
    "Statistical_report"
]

st.subheader("📌 Enter Feature Values")

input_data = []

# Create inputs dynamically
for feature in features:
    value = st.selectbox(
        f"{feature}",
        options=[-1, 0, 1],
        index=1
    )
    input_data.append(value)

# Predict button
if st.button("🔍 Predict Website"):
    prediction = model.predict([input_data])[0]

    if prediction == 1:
        st.success("✅ Legitimate Website")
    elif prediction == 0:
        st.warning("⚠ Suspicious Website")
    else:
        st.error("🚨 Phishing Website")   