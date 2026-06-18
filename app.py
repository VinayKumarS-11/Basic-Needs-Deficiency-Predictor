

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Basic Needs Deficiency Detector",
    page_icon="🏠",
    layout="wide"
)

st.markdown("""
<h1 style='text-align:center;color:#1E88E5;'>
🏠 AI Based Basic Needs Deficiency Detection System
</h1>
<h4 style='text-align:center;color:gray;'>
Government Welfare Recommendation Platform
</h4>
<hr>
""", unsafe_allow_html=True)

grade_map = {
    "A - Excellent": 90,
    "B - Good": 75,
    "C - Average": 60,
    "D - Poor": 40,
    "E - Very Poor": 20
}

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

water = grade_map[water_grade]
sanitation = grade_map[sanitation_grade]
electricity = grade_map[electricity_grade]
education = grade_map[education_grade]
nutrition = grade_map[nutrition_grade]

if st.button("Analyze", use_container_width=True):

    score = (
        water +
        sanitation +
        electricity +
        education +
        nutrition
    ) / 5

    lowest = min(
        water,
        sanitation,
        electricity,
        education,
        nutrition
    )

    deficient_areas = []

    if water < 60:
        deficient_areas.append("Water")

    if sanitation < 60:
        deficient_areas.append("Sanitation")

    if electricity < 60:
        deficient_areas.append("Electricity")

    if education < 60:
        deficient_areas.append("Education")

    if nutrition < 40:
        deficient_areas.append("Nutrition")

    if lowest < 30:
        status = "Deficient"
    elif score >= 75:
        status = "Efficient"
    elif score >= 50:
        status = "Moderate"
    else:
        status = "Deficient"

    if lowest < 20:
        priority = "Very High"
    elif lowest < 40:
        priority = "High"
    elif lowest < 60:
        priority = "Medium"
    else:
        priority = "Low"

    st.markdown("---")

    st.metric(
        "Overall Basic Needs Score",
        f"{score:.2f}%"
    )

    if status == "Efficient":
        st.success(f"Status : {status}")

    elif status == "Moderate":
        st.warning(f"Status : {status}")

    else:
        st.error(f"Status : {status}")

    st.info(f"Priority Level : {priority}")

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
            fill="toself"
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,100]
            )
        ),
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Deficient Areas")

    if deficient_areas:
        for area in deficient_areas:
            st.write("❌", area)
    else:
        st.success(
            "No major deficiencies detected."
        )

    st.subheader("Government Scheme Recommendations")

    schemes = []

    if water < 60:
        schemes.append(
            "Jal Jeevan Mission"
        )

    if sanitation < 60:
        schemes.append(
            "Swachh Bharat Mission"
        )

    if electricity < 60:
        schemes.append(
            "Saubhagya Scheme"
        )

    if education < 60:
        schemes.append(
            "Samagra Shiksha"
        )
        schemes.append(
            "PM eVIDYA"
        )

    if nutrition < 40:
        schemes.append(
            "POSHAN Abhiyaan"
        )
        schemes.append(
            "Mid-Day Meal Scheme"
        )

    if schemes:
        for s in schemes:
            st.write("✅", s)
    else:
        st.success(
            "No scheme recommendation required."
        )

    st.subheader("Improvement Suggestions")

    if water < 60:
        st.write(
            "✔ Improve clean water availability."
        )

    if sanitation < 60:
        st.write(
            "✔ Improve sanitation facilities."
        )

    if electricity < 60:
        st.write(
            "✔ Improve electricity access."
        )

    if education < 60:
        st.write(
            "✔ Improve educational resources."
        )

    if nutrition < 40:
        st.write(
            "✔ Improve food and nutrition support."
        )

    report = pd.DataFrame({
        "Parameter": categories,
        "Score": values
    })

    csv = report.to_csv(index=False)

    st.download_button(
        "Download Report",
        csv,
        "basic_needs_report.csv",
        "text/csv"
    )