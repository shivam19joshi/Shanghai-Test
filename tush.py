import streamlit as st

def calculate_bmi(weight, height):
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

st.title("BMI Calculator App")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=120, step=1)
email = st.text_input("Enter your email")
height = st.number_input("Enter your height (in cm)", min_value=50, max_value=250, step=1)
weight = st.number_input("Enter your weight (in kg)", min_value=10, max_value=300, step=1)
activity_level = st.selectbox("Select your activity level", ["Sedentary", "Lightly active", "Moderately active", "Very active"])

target_bmi = st.slider("Select your target BMI", 15.0, 30.0, 22.0, 0.1)

if st.button("Calculate BMI"):
    if name and email and height and weight:
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        st.success(f"Hello {name}, your BMI is {bmi}, which is classified as {category}.")
    else:
        st.error("Please fill in all the fields correctly.")
