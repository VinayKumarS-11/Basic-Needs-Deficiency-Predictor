import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go

# Load Model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Page Config
st.set_page_config(
    page_title="Basic Needs Efficiency Predictor",
    page_icon="🏠",
    layout="wide"
)

# Header
st.markdown("""
<h1 style='text-align:center; color:#1E88E5;'>
🏠 Basic Needs Efficiency Prediction System
</h1>
<h4 style='text-align:center; color:gray;'>
Machine Learning Based Social Welfare Assessment
</h4>
<hr>
""", unsafe_allow_html=True)

# Grade Mapping
grade_map = {
    "A - Excellent": 90,
    "B - Good": 75,
    "C - Average": 60,
    "D - Poor": 40,
    "E - Very Poor": 20
}

st.subheader("Enter Basic Needs Assessment")

col1, col2 = st.columns(2)

with col1:
    water_grade = st.selectbox(
        "💧 Water Availability",
        list(grade_map.keys())
    )

    sanitation_grade = st.selectbox(
        "🚽 Sanitation Facilities",
        list(grade_map.keys())
    )

    electricity_grade = st.selectbox(
        "⚡ Electricity Access",
        list(grade_map.keys())
    )

with col2:
    education_grade = st.selectbox(
        "🎓 Education Access",
        list(grade_map.keys())
    )

    nutrition_grade = st.selectbox(
        "🍎 Nutrition Level",
        list(grade_map.keys())
    )

# Convert Grades to Numerical Values
water = grade_map[water_grade]
sanitation = grade_map[sanitation_grade]
electricity = grade_map[electricity_grade]
education = grade_map[education_grade]
nutrition = grade_map[nutrition_grade]

# Calculate Score
score = (
    water +
    sanitation +
    electricity +
    education +
    nutrition
) / 5

st.markdown("### Overall Basic Needs Score")

st.progress(int(score))

st.metric(
    label="Score",
    value=f"{score:.2f}%"
)

# Predict
if st.button("Predict Status", use_container_width=True):

    input_data = np.array([[
        water,
        sanitation,
        electricity,
        education,
        nutrition
    ]])

    prediction = model.predict(input_data)[0]

    st.markdown("---")

    st.subheader("Prediction Result")

    if prediction == "Efficient":
        st.success(
            "🟢 BASIC NEEDS STATUS : EFFICIENT"
        )

    elif prediction == "Moderate":
        st.warning(
            "🟡 BASIC NEEDS STATUS : MODERATE"
        )

    else:
        st.error(
            "🔴 BASIC NEEDS STATUS : DEFICIENT"
        )

    st.write("### Selected Grades")

    st.write(f"💧 Water : {water_grade}")
    st.write(f"🚽 Sanitation : {sanitation_grade}")
    st.write(f"⚡ Electricity : {electricity_grade}")
    st.write(f"🎓 Education : {education_grade}")
    st.write(f"🍎 Nutrition : {nutrition_grade}")

    # Radar Chart
    categories = [
        "Water",
        "Sanitation",
        "Electricity",
        "Education",
        "Nutrition"
    ]

    values = [
        water,
        sanitation,
        electricity,
        education,
        nutrition
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            name="Assessment"
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        title="Basic Needs Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Recommendations
    st.subheader("Recommendations")

    recommendations = []

    if water < 60:
        recommendations.append(
            "Improve access to clean and safe water."
        )

    if sanitation < 60:
        recommendations.append(
            "Enhance sanitation facilities and hygiene awareness."
        )

    if electricity < 60:
        recommendations.append(
            "Improve availability of reliable electricity."
        )

    if education < 60:
        recommendations.append(
            "Increase educational opportunities and resources."
        )

    if nutrition < 60:
        recommendations.append(
            "Improve nutrition and food security programs."
        )

    if recommendations:
        for rec in recommendations:
            st.write("✔", rec)
    else:
        st.success(
            "All basic needs indicators are satisfactory."
        )

st.markdown("---")

st.info("""
Project Title:
Basic Needs Efficiency Prediction System Using Machine Learning

Algorithm:
Random Forest Classifier

Input Parameters:
• Water Availability
• Sanitation Facilities
• Electricity Access
• Education Access
• Nutrition Level

Output:
• Efficient
• Moderate
• Deficient
""")