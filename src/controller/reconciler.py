"""Kubernetes Reconciler loop."""
from ..collector.metrics_buffer import MetricsBuffer
from ..analyzer.anomaly_detector import AnomalyDetector
from ..analyzer.autoscaler import PredictiveAutoscaler

class AutoscalerReconciler:
    def __init__(self):
        self.buffer = MetricsBuffer()
        self.detector = AnomalyDetector()
        self.scaler = PredictiveAutoscaler()
        self.current_replicas = 3

    def step(self, deployment_name: str, cpu_reading: float) -> dict:
        self.buffer.record(deployment_name, cpu_reading)
        values = self.buffer.get_values(deployment_name)
        
        analysis = self.detector.evaluate(values)
        recommended = self.scaler.calculate_replicas(
            self.current_replicas,
            cpu_reading,
            analysis["is_anomaly"]
        )

        action = "NOOP"
        if recommended != self.current_replicas:
            action = f"SCALE_{'UP' if recommended > self.current_replicas else 'DOWN'}"
            self.current_replicas = recommended

        return {
            "deployment": deployment_name,
            "current_replicas": self.current_replicas,
            "analysis": analysis,
            "action": action
        }
