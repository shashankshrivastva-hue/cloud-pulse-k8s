# ☸️ CloudPulse K8s

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)](https://kubernetes.io)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)

Autonomous Kubernetes controller with statistical anomaly detection and predictive pod autoscaling.

---

## 🏛️ Architecture

```mermaid
flowchart LR
    K8s[K8s Metrics / Prometheus] -->|CPU & Mem Stream| Buffer[Rolling Window Buffer]
    Buffer --> Detector{Z-Score Anomaly Detector}
    Detector -->|Normal Load| Scaler[Proportional Scaler]
    Detector -->|Traffic Spike| ScalerBoost[Predictive Scaler Surge Boost]
    Scaler & ScalerBoost --> Operator[Reconciler Operator]
    Operator -->|K8s API Patch| Deployment[K8s Deployment Replicas]
```

## 🚀 Features

- **Rolling Z-Score Anomaly Detection**: Detects abnormal traffic spikes and DDOS patterns before standard HPAs respond.
- **Predictive Autoscaling**: Anticipates capacity saturation and pre-warms replica pods.
- **Helm Ready**: Includes production Helm chart and containerized runtime.

## 🛠️ Usage

```bash
pip install -r requirements.txt
pytest tests/ -v
uvicorn src.api.server:app --port 8000
```

## 📜 License
MIT License. Built by [Shashank Shrivastva](https://github.com/shashankshrivastva-hue).
