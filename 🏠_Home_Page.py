import streamlit as st

st.set_page_config(
    page_title = "Burnt Calorie Prediction App",
    page_icon  = "🔥",
)

st.markdown("<h1 style='text-align: center; color: #FF5733;'>🔥Burnt Calorie Prediction App🔥</h1>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style="font-size:18px;">
Welcome to the <b>Burnt Calorie Prediction App</b>! 🌟<br><br>

This application predicts the number of calories you burn during a workout session based on the following factors:
<ul>
    <li><b>Gender</b></li>
    <li><b>Age</b></li>
    <li><b>Height</b></li>
    <li><b>Weight</b></li>
    <li><b>Duration of Workout</b></li>
    <li><b>Heart Rate</b></li>
    <li><b>Body Temperature</b></li>
</ul>

We use a <span style="color:green;"><b>machine learning model</b></span> trained with 
<span style="color:green;"><b>99% accuracy</b></span> to provide you with fast, reliable predictions. 🚀
<br><br>

<h3 style="color:#17A589;">✨ How to Use:</h3>
<ol>
    <li>Go to the <b>Prediction</b> page.</li>
    <li>Fill in your personal and workout details.</li>
    <li>Click <b>Predict</b> to see your estimated burnt calories!</li>
</ol>

Let's get started! 🎯
</div>
""", unsafe_allow_html=True)
