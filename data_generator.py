from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def generate_healthcare_dataset(rows: int = 1000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    age = rng.integers(18, 90, rows)
    bmi = np.round(rng.normal(26, 5, rows).clip(15, 45), 1)
    systolic_bp = rng.integers(95, 190, rows)
    diastolic_bp = rng.integers(55, 120, rows)
    heart_rate = rng.integers(50, 135, rows)
    glucose = rng.integers(70, 240, rows)
    oxygen_saturation = rng.integers(82, 100, rows)
    sleep_hours = np.round(rng.normal(6.8, 1.4, rows).clip(3, 10), 1)
    activity_minutes = rng.integers(0, 150, rows)
    symptom_severity = rng.integers(0, 11, rows)
    chronic_condition = rng.integers(0, 2, rows)

    risk_score = (
        (age >= 60) * 2.0
        + (bmi >= 30) * 1.5
        + (systolic_bp >= 140) * 2.0
        + (diastolic_bp >= 90) * 1.5
        + (heart_rate >= 110) * 1.5
        + (glucose >= 160) * 2.0
        + (oxygen_saturation <= 92) * 2.5
        + (sleep_hours <= 5.5) * 1.0
        + (activity_minutes <= 20) * 1.0
        + (symptom_severity >= 7) * 2.5
        + (chronic_condition == 1) * 1.5
        + rng.normal(0, 0.6, rows)
    )

    risk_level = np.select(
        [risk_score < 4.0, (risk_score >= 4.0) & (risk_score < 8.0), risk_score >= 8.0],
        [0, 1, 2],
    )

    return pd.DataFrame(
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
            "risk_level": risk_level.astype(int),
        }
    )


def save_dataset(output_path: Path, rows: int = 1000, seed: int = 42) -> Path:
    dataset = generate_healthcare_dataset(rows=rows, seed=seed)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataset.to_csv(output_path, index=False)
    return output_path


if __name__ == "__main__":
    destination = Path("artifacts/dataset.csv")
    save_dataset(destination)
    print(f"Dataset saved to {destination}")
