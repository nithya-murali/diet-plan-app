import streamlit as st

# Set the page title
st.set_page_config(page_title="Personalized Diet Plan", layout="centered")

# Header
st.title("Personalized Diet Plan")

with st.form("diet_form"):
    # Basic Information
    st.subheader("Basic Information")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    height = st.number_input("Height (cm)", min_value=50, max_value=250, step=1)
    weight = st.number_input("Weight (kg)", min_value=10, max_value=300, step=1)
    body_fat = st.slider("Body Fat Percentage", min_value=0, max_value=50, step=1)

    # Activity Level
    st.subheader("Activity Level")
    activity_level = st.selectbox("Select your activity level", 
                                  ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])

    # Health & Medical Background
    st.subheader("Health & Medical Background")
    conditions = st.multiselect("Do you have any health conditions?", 
                                ["Diabetes", "Hypertension", "PCOS", "Thyroid Issues", "None"])
    medications = st.text_area("Medications/Supplements (if any)")

    # Dietary Preferences
    st.subheader("Dietary Preferences & Restrictions")
    diet_type = st.selectbox("Preferred Diet Type", 
                             ["No Preference", "Vegetarian", "Vegan", "Keto", "Paleo", "Mediterranean"])
    allergies = st.text_input("Food Allergies/Intolerances")
    dislikes = st.text_input("Foods You Dislike")

    # Goals & Lifestyle
    st.subheader("Goals & Lifestyle")
    goal = st.selectbox("Primary Goal", ["Weight Loss", "Muscle Gain", "Maintenance", "Improve Energy"])
    target_weight = st.number_input("Target Weight (kg)", min_value=10, max_value=300, step=1)
    meal_timing = st.selectbox("Meal Timing", ["Regular (3 meals/day)", "Intermittent Fasting", "Flexible"])
    cooking_habits = st.radio("Do you cook at home?", ["Yes", "No", "Sometimes"])

    # Additional Factors
    st.subheader("Additional Considerations")
    hydration = st.slider("Average Daily Water Intake (Liters)", min_value=0.5, max_value=5.0, step=0.1)
    sleep_hours = st.slider("Average Sleep per Night (Hours)", min_value=3, max_value=12, step=1)
    stress_level = st.selectbox("Stress Level", ["Low", "Moderate", "High"])

    # Submit button
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.success("Form submitted successfully!")
        st.write("### Entered Details:")
        st.json({
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Height (cm)": height,
            "Weight (kg)": weight,
            "Body Fat (%)": body_fat,
            "Activity Level": activity_level,
            "Health Conditions": conditions,
            "Medications/Supplements": medications,
            "Diet Type": diet_type,
            "Allergies": allergies,
            "Disliked Foods": dislikes,
            "Primary Goal": goal,
            "Target Weight (kg)": target_weight,
            "Meal Timing": meal_timing,
            "Cooking Habits": cooking_habits,
            "Hydration (L/day)": hydration,
            "Sleep (hours/night)": sleep_hours,
            "Stress Level": stress_level
        })
