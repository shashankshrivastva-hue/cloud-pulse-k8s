"""Statistical anomaly detection using rolling Z-Score."""
import numpy as np
from typing import Optional, Dict, Any

class AnomalyDetector:
    def __init__(self, z_threshold: float = 2.5):
        self.z_threshold = z_threshold

    def evaluate(self, values: list[float]) -> Dict[str, Any]:
        if len(values) < 5:
            return {"is_anomaly": False, "z_score": 0.0, "mean": 0.0, "std": 0.0}

        arr = np.array(values)
        mean = float(np.mean(arr[:-1]))
        std = float(np.std(arr[:-1]))
        latest = arr[-1]

        if std == 0.0:
            return {"is_anomaly": False, "z_score": 0.0, "mean": mean, "std": 0.0}

        z_score = float((latest - mean) / std)
        is_anomaly = abs(z_score) >= self.z_threshold

        return {
            "is_anomaly": is_anomaly,
            "z_score": round(z_score, 3),
            "latest_val": round(float(latest), 2),
            "mean": round(mean, 2),
            "std": round(std, 2)
        }
