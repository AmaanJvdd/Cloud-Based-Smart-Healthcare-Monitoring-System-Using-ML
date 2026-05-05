# Cloud-Based Smart Healthcare Monitoring System Using ML Without IoT Devices

This project is a smart healthcare monitoring system that predicts a patient's health risk level using machine learning and cloud-friendly software workflows, without relying on IoT devices.

Instead of collecting data from wearable sensors, the system uses manually entered clinical and lifestyle data such as age, BMI, blood pressure, heart rate, glucose level, oxygen saturation, sleep duration, activity level, and symptom severity. The trained ML model analyzes these inputs and predicts whether the patient's condition is `Low`, `Medium`, or `High` risk.

## Project Objective

To build a cloud-based healthcare monitoring solution that helps doctors, clinics, telemedicine teams, and health platforms assess patient risk quickly using machine learning, even when IoT devices are not available.

## Key Features

- Predicts patient health risk using a machine learning model
- Works without IoT devices or wearable sensors
- Uses synthetic healthcare data for training and testing
- Streamlit-based dashboard for simple interaction
- Auto-generates training data and model artifacts when missing
- Suitable for academic demos, mini-projects, and final-year presentations

## Technology Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

## Project Structure

```text
.
|-- app.py
|-- requirements.txt
|-- README.md
|-- PROJECT_REPORT.md
|-- .gitignore
|-- src/
|   |-- data_generator.py
|   |-- model_utils.py
|   `-- train_model.py
`-- artifacts/
    |-- dataset.csv
    |-- model.joblib
    `-- metrics.json
```

## How It Works

1. Synthetic patient data is generated using realistic healthcare-related ranges.
2. A machine learning model is trained to classify health risk levels.
3. The trained model is stored in the `artifacts/` folder.
4. Users open the Streamlit app and enter patient details.
5. The system predicts the patient's risk category and shows recommended actions.

## Installation

```bash
pip install -r requirements.txt
```

## Run The App

```bash
streamlit run app.py
```

## Train The Model Manually

```bash
python3 src/train_model.py
```

## Example Use Cases

- Remote patient pre-screening
- Telemedicine consultation support
- Hospital triage assistance
- College final-year ML project demonstration
- Healthcare analytics prototype for cloud deployment

## Future Enhancements

- User authentication for doctors and patients
- Cloud database integration
- PDF health report generation
- Appointment scheduling and alert modules
- Real patient dataset integration
- Deployment on Streamlit Cloud, Render, or AWS

## Note

This project uses synthetic data for educational purposes and is not intended for real clinical diagnosis.
