"""Rolling time-series buffer for CPU and memory telemetry."""
import time
from collections import deque
from typing import Dict, List, Tuple

class MetricsBuffer:
    def __init__(self, window_size: int = 60):
        self.window_size = window_size
        self._buffers: Dict[str, deque] = {}

    def record(self, metric_name: str, value: float, timestamp: float = None):
        if timestamp is None:
            timestamp = time.time()
        if metric_name not in self._buffers:
            self._buffers[metric_name] = deque(maxlen=self.window_size)
        self._buffers[metric_name].append((timestamp, value))

    def get_series(self, metric_name: str) -> List[Tuple[float, float]]:
        return list(self._buffers.get(metric_name, []))

    def get_values(self, metric_name: str) -> List[float]:
        return [v for _, v in self._buffers.get(metric_name, [])]
