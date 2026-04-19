from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from src.model_utils import train_and_save_model


if __name__ == "__main__":
    metrics = train_and_save_model()
    print("Model training completed.")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
