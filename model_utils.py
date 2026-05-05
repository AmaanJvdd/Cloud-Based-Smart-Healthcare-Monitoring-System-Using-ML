from __future__ import annotations

import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from src.data_generator import save_dataset


BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
DATASET_PATH = ARTIFACTS_DIR / "dataset.csv"
MODEL_PATH = ARTIFACTS_DIR / "model.joblib"
METRICS_PATH = ARTIFACTS_DIR / "metrics.json"

FEATURE_COLUMNS = [
    "age",
    "bmi",
    "systolic_bp",
    "diastolic_bp",
    "heart_rate",
    "glucose",
    "oxygen_saturation",
    "sleep_hours",
    "activity_minutes",
    "symptom_severity",
    "chronic_condition",
]

LABEL_MAPPING = {
    0: "Low",
    1: "Medium",
    2: "High",
}


def train_and_save_model(rows: int = 1000, seed: int = 42) -> dict:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    save_dataset(DATASET_PATH, rows=rows, seed=seed)

    dataset = pd.read_csv(DATASET_PATH)
    X = dataset[FEATURE_COLUMNS]
    y = dataset["risk_level"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=seed,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        min_samples_split=4,
        random_state=seed,
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(
        y_test,
        predictions,
        target_names=[LABEL_MAPPING[0], LABEL_MAPPING[1], LABEL_MAPPING[2]],
        output_dict=True,
    )

    joblib.dump(model, MODEL_PATH)

    metrics = {
        "accuracy": accuracy,
        "rows": len(dataset),
        "model_name": "RandomForestClassifier",
        "class_report": report,
    }

    with METRICS_PATH.open("w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=2)

    return metrics


def ensure_artifacts() -> None:
    if not DATASET_PATH.exists() or not MODEL_PATH.exists() or not METRICS_PATH.exists():
        train_and_save_model()


def load_metrics() -> dict:
    ensure_artifacts()
    with METRICS_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)
