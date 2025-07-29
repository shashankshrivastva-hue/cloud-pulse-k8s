from src.analyzer.anomaly_detector import AnomalyDetector
from src.analyzer.autoscaler import PredictiveAutoscaler

def test_anomaly_detection():
    detector = AnomalyDetector(z_threshold=2.0)
    # Baseline steady traffic
    baseline = [50.0, 52.0, 49.0, 51.0, 50.0, 50.5]
    assert not detector.evaluate(baseline)["is_anomaly"]

    # Sudden spike
    spike = baseline + [95.0]
    res = detector.evaluate(spike)
    assert res["is_anomaly"] is True

def test_predictive_scaling():
    scaler = PredictiveAutoscaler(target_cpu_utilization=50.0, min_replicas=2, max_replicas=10)
    # Normal load
    assert scaler.calculate_replicas(4, 50.0, False) == 4
    # Double load
    assert scaler.calculate_replicas(4, 100.0, False) == 8
    # Anomaly boost
    assert scaler.calculate_replicas(4, 100.0, True) == 10
