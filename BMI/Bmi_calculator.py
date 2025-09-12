import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# --- Custom CSS for Light Theme ---
st.markdown("""
<style>
    .stApp {
        background-color: #f8f9fa;  /* Light background */
        color: #212529;  /* Dark text */
    }
    .result-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: white; /* For readability */
    }
    .underweight { background-color: #5dade2; }
    .normal { background-color: #58d68d; }
    .overweight { background-color: #f5b041; }
    .obese { background-color: #ec7063; }
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("⚖️ BMI Calculator")

# --- Weight Input ---
weight = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=500.0, value=70.0)

# --- Height Input with Units ---
unit = st.radio("Select Height Unit:", ["Meters", "Centimeters", "Feet/Inches"])

if unit == "Meters":
    height_m = st.number_input("Enter your height (meters)", min_value=0.5, max_value=3.0, value=1.70)
elif unit == "Centimeters":
    height_cm = st.number_input("Enter your height (cm)", min_value=50.0, max_value=300.0, value=170.0)
    height_m = height_cm / 100
else:  # Feet/Inches
    height_ft = st.number_input("Enter feet", min_value=1, max_value=8, value=5)
    height_in = st.number_input("Enter inches", min_value=0, max_value=11, value=7)
    height_m = (height_ft * 12 + height_in) * 0.0254  # Convert to meters

# --- BMI Calculation ---
if st.button("Calculate BMI"):
    if height_m > 0:
        bmi = weight / (height_m ** 2)

        # --- BMI Category ---
        if bmi < 18.5:
            category = "Underweight"
            css_class = "underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
            css_class = "normal"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            css_class = "overweight"
        else:
            category = "Obese"
            css_class = "obese"

        # --- Healthy Weight Range (kg) ---
        min_weight = 18.5 * (height_m ** 2)
        max_weight = 24.9 * (height_m ** 2)

        result_text = (
            f"Your BMI is **{bmi:.2f}** ({category}).\n\n"
            f"✅ Healthy weight range for your height: **{min_weight:.1f} kg – {max_weight:.1f} kg**"
        )

        # --- Show Result ---
        st.markdown(
            f"<div class='result-box {css_class}'>Your BMI is <b>{bmi:.2f}</b> ({category})</div>",
            unsafe_allow_html=True
        )
        st.success(f"Healthy weight range for your height: {min_weight:.1f} kg – {max_weight:.1f} kg")

        # --- Copy to Clipboard ---
        st.code(result_text, language="markdown")
        
        

    else:
        st.error("Height must be greater than 0!")
