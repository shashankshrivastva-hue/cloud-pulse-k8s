"""Predictive replica scaling calculations."""
import math

class PredictiveAutoscaler:
    def __init__(self, target_cpu_utilization: float = 70.0, min_replicas: int = 2, max_replicas: int = 20):
        self.target_cpu = target_cpu_utilization
        self.min_replicas = min_replicas
        self.max_replicas = max_replicas

    def calculate_replicas(self, current_replicas: int, current_cpu_avg: float, anomaly_flag: bool) -> int:
        if current_replicas <= 0:
            return self.min_replicas

        # Base proportional scaling
        ratio = current_cpu_avg / self.target_cpu
        desired = math.ceil(current_replicas * ratio)

        # Proactive scaling boost if anomaly detected
        if anomaly_flag:
            desired = math.ceil(desired * 1.5)

        # Clamping
        return max(self.min_replicas, min(desired, self.max_replicas))
