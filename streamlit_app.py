import streamlit as st
from openai import OpenAI

client = OpenAI(
  api_key="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"
)

# Set the page title
# Title the app
st.title('Personalized Diet Plan')

st.markdown("""
 * Use the menu at left to input information of bodyvitals and diet preferences
 * And Hang tight while we whip up a personalized diet plan just for you—healthy, tasty, and totally on point! 🍏🥗✨
""")

with st.sidebar.form("diet_form"):
    # Basic Information
    st.sidebar.markdown("## Basic Information")
    name = st.sidebar.text_input("Name")
    age = st.sidebar.number_input("Age", min_value=1, max_value=120, step=1)
    gender = st.sidebar.radio("Gender", ["Male", "Female", "Other"])
    height = st.sidebar.number_input("Height (cm)", min_value=50, max_value=250, step=1)
    weight = st.sidebar.number_input("Weight (kg)", min_value=10, max_value=300, step=1)
    body_fat = st.sidebar.slider("Body Fat Percentage", min_value=0, max_value=50, step=1)

    # Activity Level
    st.sidebar.markdown("## Activity Level")
    activity_level = st.sidebar.selectbox("Select your activity level", 
                                  ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])

    # Health & Medical Background
    st.sidebar.markdown("## Health & Medical Background")
    conditions = st.sidebar.multiselect("Do you have any health conditions?", 
                                ["Diabetes", "Hypertension", "PCOS", "Thyroid Issues", "None"])
    medications = st.sidebar.text_area("Medications/Supplements (if any)")

    # Dietary Preferences
    st.sidebar.markdown("## Dietary Preferences & Restrictions")
    diet_type = st.sidebar.selectbox("Preferred Diet Type", 
                             ["No Preference", "Vegetarian", "Vegan", "Keto", "Paleo", "Mediterranean"])
    allergies = st.sidebar.text_input("Food Allergies/Intolerances")
    dislikes = st.sidebar.text_input("Foods You Dislike")

    # Goals & Lifestyle
    st.sidebar.markdown("## Goals & Lifestyle")
    goal = st.sidebar.selectbox("Primary Goal", ["Weight Loss", "Muscle Gain", "Maintenance", "Improve Energy"])
    target_weight = st.sidebar.number_input("Target Weight (kg)", min_value=10, max_value=300, step=1)
    meal_timing = st.sidebar.selectbox("Meal Timing", ["Regular (3 meals/day)", "Intermittent Fasting", "Flexible"])
    cooking_habits = st.sidebar.radio("Do you cook at home?", ["Yes", "No", "Sometimes"])

    # Additional Factors
    st.sidebar.markdown("## Additional Considerations")
    hydration = st.sidebar.slider("Average Daily Water Intake (Liters)", min_value=0.5, max_value=5.0, step=0.1)
    sleep_hours = st.sidebar.slider("Average Sleep per Night (Hours)", min_value=3, max_value=12, step=1)
    stress_level = st.sidebar.selectbox("Stress Level", ["Low", "Moderate", "High"])

    # Submit button
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.success("Hang tight! We're whipping up a personalized diet plan just for you—healthy, tasty, and totally on point! 🍏🥗✨")

user_info = {
            "name": name,
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight,
            "body_fat": body_fat,
            "activity_level": activity_level,
            "conditions": conditions,
            "medications": medications,
            "diet_type": diet_type,
            "allergies": allergies,
            "dislikes": dislikes,
            "goal": goal,
            "target_weight": target_weight,
            "meal_timing": meal_timing,
            "cooking_habits": cooking_habits,
            "hydration": hydration,
            "sleep_hours": sleep_hours,
            "stress_level": stress_level
        }
            
def get_diet_plan(user_data):
    """
    Connects to OpenAI's GPT model and generates a personalized diet plan based on user inputs.
    """
    prompt = f"""
    Create a personalized diet plan based on the following details:
    
    Name: {user_data['name']}
    Age: {user_data['age']}
    Gender: {user_data['gender']}
    Height: {user_data['height']} cm
    Weight: {user_data['weight']} kg
    Body Fat Percentage: {user_data['body_fat']}%
    Activity Level: {user_data['activity_level']}
    Health Conditions: {', '.join(user_data['conditions']) if user_data['conditions'] else 'None'}
    Medications/Supplements: {user_data['medications']}
    Preferred Diet Type: {user_data['diet_type']}
    Food Allergies: {user_data['allergies']}
    Foods Disliked: {user_data['dislikes']}
    Primary Goal: {user_data['goal']}
    Target Weight: {user_data['target_weight']} kg
    Meal Timing Preference: {user_data['meal_timing']}
    Cooking Habit: {user_data['cooking_habits']}
    Hydration Level: {user_data['hydration']} L/day
    Sleep Duration: {user_data['sleep_hours']} hours/night
    Stress Level: {user_data['stress_level']}
    
    Based on this information, suggest a **detailed daily meal plan** including:
    - Breakfast
    - Lunch
    - Dinner
    - Snacks
    - Hydration tips
    - Additional lifestyle suggestions for better health.
    """

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "system", "content": "You are a professional nutritionist providing expert diet plans."},
        {"role": "user", "content": prompt}
    ])

    return response["choices"][0]["message"]["content"]



# Get diet plan recommendation
diet_plan = get_diet_plan(user_info)
st.write(diet_plan)


