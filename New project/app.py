from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

from src.model_utils import (
    ARTIFACTS_DIR,
    FEATURE_COLUMNS,
    LABEL_MAPPING,
    ensure_artifacts,
    load_metrics,
)


st.set_page_config(
    page_title="Smart Healthcare Monitoring",
    page_icon="+",
    layout="wide",
)


def load_model():
    ensure_artifacts()
    return joblib.load(ARTIFACTS_DIR / "model.joblib")


def build_input_frame(form_values: dict) -> pd.DataFrame:
    return pd.DataFrame([form_values], columns=FEATURE_COLUMNS)


def recommendation_for_risk(risk_label: str) -> str:
    recommendations = {
        "Low": "Maintain healthy routines and continue regular checkups.",
        "Medium": "Monitor the patient more closely and recommend a medical consultation soon.",
        "High": "Immediate clinical review is recommended for further examination and intervention.",
    }
    return recommendations[risk_label]


st.title("Cloud-Based Smart Healthcare Monitoring System Using ML")
st.caption(
    "A machine learning project for predicting patient health risk using manual healthcare inputs."
)

model = load_model()
metrics = load_metrics()

left, right = st.columns([1.2, 0.8])

with right:
    st.subheader("Model Snapshot")
    st.metric("Validation Accuracy", f"{metrics['accuracy'] * 100:.2f}%")
    st.metric("Training Records", metrics["rows"])
    st.metric("Model Type", metrics["model_name"])
    st.info("This demo uses synthetic healthcare data for educational use.")

with left:
    st.subheader("Enter Patient Details")
    with st.form("patient_form"):
        age = st.slider("Age", 18, 90, 45)
        bmi = st.slider("BMI", 15.0, 45.0, 24.5, 0.1)
        systolic_bp = st.slider("Systolic Blood Pressure", 90, 200, 120)
        diastolic_bp = st.slider("Diastolic Blood Pressure", 50, 130, 80)
        heart_rate = st.slider("Heart Rate", 45, 140, 78)
        glucose = st.slider("Glucose Level", 70, 250, 105)
        oxygen_saturation = st.slider("Oxygen Saturation", 80, 100, 97)
        sleep_hours = st.slider("Sleep Hours", 3.0, 10.0, 7.0, 0.5)
        activity_minutes = st.slider("Daily Activity Minutes", 0, 180, 35)
        symptom_severity = st.slider("Symptom Severity (0-10)", 0, 10, 3)
        chronic_condition = st.selectbox("Chronic Condition History", [0, 1], format_func=lambda x: "Yes" if x else "No")

        submitted = st.form_submit_button("Predict Risk")

if submitted:
    input_df = build_input_frame(
        {
            "age": age,
            "bmi": bmi,
            "systolic_bp": systolic_bp,
            "diastolic_bp": diastolic_bp,
            "heart_rate": heart_rate,
            "glucose": glucose,
            "oxygen_saturation": oxygen_saturation,
            "sleep_hours": sleep_hours,
            "activity_minutes": activity_minutes,
            "symptom_severity": symptom_severity,
            "chronic_condition": chronic_condition,
        }
    )

    prediction = int(model.predict(input_df)[0])
    probabilities = model.predict_proba(input_df)[0]
    risk_label = LABEL_MAPPING[prediction]

    st.success(f"Predicted Risk Level: {risk_label}")
    st.write(recommendation_for_risk(risk_label))

    probability_frame = pd.DataFrame(
        {
            "Risk Level": [LABEL_MAPPING[index] for index in range(len(probabilities))],
            "Confidence": probabilities,
        }
    )
    st.subheader("Prediction Confidence")
    st.bar_chart(probability_frame.set_index("Risk Level"))

    st.subheader("Submitted Patient Record")
    st.dataframe(input_df, use_container_width=True)

st.divider()
st.subheader("Why This Project Is Different")
st.write(
    """
    This system is designed for healthcare monitoring without relying on IoT devices.
    It is suitable for cloud deployment, telemedicine workflows, and academic machine learning demonstrations.
    """
)

artifacts_path = Path(ARTIFACTS_DIR)
st.caption(f"Artifacts directory: {artifacts_path}")
