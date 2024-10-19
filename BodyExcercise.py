import streamlit as st
from PIL import Image

# Placeholder function to classify body type (you can replace this with a real model)
def classify_body_type(image):
    # Dummy classification logic based on image dimensions (as a placeholder)
    width, height = image.size
    aspect_ratio = width / height

    if aspect_ratio > 0.8:
        return "Mesomorph"
    elif aspect_ratio < 0.7:
        return "Ectomorph"
    else:
        return "Endomorph"

# Function to provide exercise plan based on body type
def get_exercise_plan(body_type):
    plans = {
        "Mesomorph": """
        **Exercise Plan for Mesomorph:**
        - Strength Training: 4-5 times per week.
        - Cardio: 3 times per week (moderate intensity).
        - Focus: Balanced mix of strength and endurance exercises.
        """,
        "Ectomorph": """
        **Exercise Plan for Ectomorph:**
        - Strength Training: 3-4 times per week (high weight, low reps).
        - Cardio: Limited to 1-2 times per week (low intensity).
        - Focus: Muscle gain with calorie surplus diet.
        """,
        "Endomorph": """
        **Exercise Plan for Endomorph:**
        - Strength Training: 4-5 times per week (moderate weight, high reps).
        - Cardio: 5 times per week (high intensity, HIIT).
        - Focus: Fat loss with a focus on full-body workouts.
        """
    }
    return plans.get(body_type, "No specific exercise plan available.")

# Streamlit app layout
st.title("Get Your Personalized Exercise Plan")
st.write("Upload an image of your body to receive an exercise plan based on your body type.")

# Image upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Classify body type (using the placeholder function)
    body_type = classify_body_type(image)

    # Display body type
    st.write(f"**Detected Body Type:** {body_type}")

    # Provide exercise plan based on body type
    exercise_plan = get_exercise_plan(body_type)
    st.write(exercise_plan)
else:
    st.write("Please upload an image to receive your exercise plan.")
