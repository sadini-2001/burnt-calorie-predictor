import pandas as pd
import streamlit as st
import joblib

# Load model
model = joblib.load("model/model.pkl")

st.title("💪Get Fit, Get Results: Accurate Burnt Calorie Predictions!")
st.markdown("---")

# Create two columns for a neat form
col1, col2 = st.columns(2)

with st.form('prediction_form'):
    with col1:
        gender = st.selectbox('👤 Gender', ['Male', 'Female'])
        age = st.number_input('🎂 Age')
        height = st.number_input('📏 Height (cm)')
        weight = st.number_input('⚖️ Weight (kg)')

    with col2:
        duration = st.number_input('🏋️‍♀️ Duration (minutes)')
        heart_rate = st.number_input('❤️ Heart Rate (bpm)')
        body_temp = st.number_input('🌡️ Body Temperature (°C)')

    submit = st.form_submit_button('Predict')

if submit:
    # Prepare input as model accepts
    input_data = pd.DataFrame(
        [[gender.lower(), age, height, weight, duration, heart_rate, body_temp]],
        columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
    )

    try:
        # Predict
        prediction = model.predict(input_data)[0]

        # Results
        st.metric(label="Estimated Calories Burnt 🔥:", value=f"{prediction:.2f} kcal", delta=None)

    except Exception as e:
        st.error(f"❌ Prediction Error: {str(e)}")
