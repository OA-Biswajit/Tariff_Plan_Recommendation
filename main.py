import streamlit as st
import joblib
import numpy as np

# -------------------------------
# Load the Decision Tree Model
# -------------------------------


model = joblib.load("tariff_recomend.pkl")


# -------------------------------
# Prediction Function
# -------------------------------
def model_prediction(total_mins, intl_mins, total_calls, intl_calls, vmail_message):
    # Convert inputs into numpy array
    input_data = np.array([[total_mins, intl_mins, total_calls, intl_calls, vmail_message]])
    prediction = model.predict(input_data)
    return prediction[0]

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Tariff Plan Recommender", page_icon="📊", layout="centered")

st.title("📊 Tariff Plan Recommender System")
st.markdown("""
Welcome! Please enter the usage details below, and the system will recommend the best tariff plan.
""")

# Sidebar

# --- Simple Auth ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Hardcoded credentials
ALLOWED_MOBILE = "382-4657"
ALLOWED_PASS = "pass123"

def login_form():
    st.header("Login")
    mobile = st.text_input("Mobile Number")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if mobile == ALLOWED_MOBILE and password == ALLOWED_PASS:
            st.session_state['authenticated'] = True
            st.success("Login successful!")
        else:
            st.error("Invalid mobile number or password.")
    if st.session_state.get('authenticated', False):
        if st.button("Go to Home"):
            st.session_state['app_mode'] = "Home"
            st.experimental_rerun()

# Navigation

if not st.session_state['authenticated']:
    login_form()
    st.stop()

# Set default app_mode after login
if 'app_mode' not in st.session_state:
    st.session_state['app_mode'] = "Home"

st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose the App mode", ["Home", "About", "Prediction"], index=["Home", "About", "Prediction"].index(st.session_state['app_mode']))
st.session_state['app_mode'] = app_mode

# Home Page
if app_mode == "Home":
    st.header("Home")
    st.image("page_photo.png", use_column_width=True)
    st.markdown("""
    This is a demo application that uses a **Decision Tree Classifier** 
    trained on telecom usage data to recommend tariff plans.  
    Navigate to the **Prediction** page to test the model.
    """)

# About Page
elif app_mode == "About":
    st.header("About")
    st.markdown("""
    - **Model**: Decision Tree Classifier  
    - **Input Features**:  
        1. Total_Mins  
        2. Intl Mins  
        3. Total_Calls  
        4. Intl Calls  
        5. VMail Message  
    - **Output**: Recommended Tariff Plan  
    """)

# Prediction Page
elif app_mode == "Prediction":
    st.header("Tariff Plan Prediction")

    # Input fields
    total_mins = st.number_input("📞 Total Mins", min_value=0.0, step=1.0)
    intl_mins = st.number_input("🌍 Intl Mins", min_value=0.0, step=0.1)
    total_calls = st.number_input("📱 Total Calls", min_value=0, step=1)
    intl_calls = st.number_input("🌐 Intl Calls", min_value=0, step=1)
    vmail_message = st.number_input("📩 VMail Message", min_value=0, step=1)

    if st.button("Predict Tariff Plan"):
        with st.spinner("Predicting..."):
            prediction = model_prediction(total_mins, intl_mins, total_calls, intl_calls, vmail_message)

        st.success(f"✅ Recommended Tariff Plan: **{prediction}**")
        # Top 3 Plans mapping (example, update with your actual mapping)
        cluster_to_top3 = {
            0: [("Basic Saver", 199), ("Standard", 399), ("Premium", 599)],
            1: [("Global Connect", 499), ("Saver Plus", 299), ("Standard Intl", 399)],
            2: [("Family Pack", 599), ("Basic Global", 299), ("Standard", 399)],
            3: [("Premium", 599), ("Saver Plus", 299), ("Basic Saver", 199)],
            4: [("Standard Intl", 399), ("Global Connect", 499), ("Family Pack", 599)],
            5: [("Basic Saver", 199), ("Basic Global", 299), ("Standard", 399)],
            6: [("Saver Plus", 299), ("Premium", 599), ("Standard", 399)],
            7: [("Global Connect", 499), ("Family Pack", 599), ("Basic Saver", 199)],
            8: [("Standard", 399), ("Basic Global", 299), ("Saver Plus", 299)],
            9: [("Basic Saver", 199), ("Basic Global", 299), ("Standard", 399)],
            10: [("Premium", 599), ("Global Connect", 499), ("Standard Intl", 399)],
            11: [("Family Pack", 599), ("Saver Plus", 299), ("Basic Saver", 199)],
            12: [("Standard Intl", 399), ("Basic Global", 299), ("Premium", 599)],
            13: [("Global Connect", 499), ("Standard", 399), ("Family Pack", 599)],
            14: [("Saver Plus", 299), ("Basic Saver", 199), ("Standard Intl", 399)],
            15: [("Premium", 599), ("Basic Global", 299), ("Global Connect", 499)],
            16: [("Family Pack", 599), ("Standard", 399), ("Saver Plus", 299)],
            17: [("Standard Intl", 399), ("Global Connect", 499), ("Basic Saver", 199)],
            18: [("Standard", 399), ("Standard Intl", 499), ("Basic Saver", 199)],
            19: [("Premium", 599), ("Saver Plus", 299), ("Family Pack", 599)],
        }
        top3_plans = cluster_to_top3.get(prediction, [])
        if top3_plans:
            st.markdown("**Top 3 Recommended Plans:**")
            for plan, price in top3_plans:
                st.write(f"{plan}: ₹{price}")
                
        else:
            st.warning("No Top 3 Plans found for this cluster.")

# -------------------------------
# Footer
# -------------------------------