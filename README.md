# ai-autonomus-devops

An intelligent self-healing DevOps system that detects incidents, analyzes logs using AI (LLM), and automatically performs remediation actions.

---

## 🚀 Overview

This project demonstrates a fully automated DevOps incident response system:

- 🔍 Monitors application health & Kubernetes logs  
- 🤖 Uses LLM (Ollama - Local AI) for decision making  
- ⚙️ Executes automated remediation (self-healing)  
- 🔄 Runs continuously with smart trigger control  

---

## 🧠 Architecture

Monitoring → Temporal Workflow → LLM (Ollama) → Decision → Activity → Fix

---

## ⚙️ Tech Stack

- Temporal (Workflow Orchestration)  
- Kubernetes (K8s - kind)  
- Docker  
- FastAPI  
- Ollama (Local LLM - llama3.2:1b)  
- Python  

---

## 🔥 Key Features

- AI-based incident analysis (no hardcoded rules)  
- Automatic remediation (self-healing system)  
- Kubernetes integration  
- Local LLM (no cost, no AWS dependency)  
- Smart monitoring (no duplicate triggers)  
- Scalable architecture  

---

## 📊 Workflow

1. Monitoring detects log changes


2. Workflow is triggered


3. Logs sent to LLM


4. LLM decides action


5. Workflow maps action → activity


6. Activity executes fix


7. System recovers automatically



---

## 🧪 Scenarios Covered

### 🔴 API Failure
- Detection: API health failure logs  
- Action: restart_api  

### 💥 Pod Crash (CrashLoopBackOff)
- Detection: Kubernetes logs  
- Action: restart_pod  

### ⚙️ CI/CD Failure
- Detection: Pipeline error logs  
- Action: retry_pipeline  

### 📈 High CPU Usage
- Detection: Performance logs  
- Action: scale_service  

### 🐳 Docker Failure
- Detection: Container errors  
- Action: restart_docker  

---

## 🤖 AI Decision Example

Input Logs:

Error: CrashLoopBackOff
Container failed to start

LLM Output:

restart_pod

---

## 📁 Project Structure

ai-autonomous-devops/ │ ├── agent/ │   └── incident_agent.py │ ├── activities/ │   ├── llm_activity.py │   ├── kubernetes_fix.py │   ├── docker_fix.py │   ├── cicd_fix.py │   ├── cpu_fix.py │   └── api_fix.py │ ├── workflows/ │   └── incident_workflow.py │ ├── monitoring/ │   └── monitor.py │ ├── worker/ │   └── worker.py │ └── app/ └── FastAPI service

---

## ⚡ Setup Instructions

### 1. Start Temporal

temporal server start-dev

### 2. Start Worker

python3 -m worker.worker

### 3. Start Monitoring

python3 -m monitoring.monitor

### 4. Run Ollama

ollama run llama3.2:1b

### 5. Deploy Application (Kubernetes)

kubectl apply -f k8s/deployment.yaml kubectl apply -f k8s/service.yaml

---

## 🧪 Testing

### Simulate API Failure

kubectl scale deployment ai-devops-app --replicas=0

### Simulate Pod Crash

kubectl delete pod -l app=ai-devops

### Watch Recovery

kubectl get pods -w

---

## 📸 Screenshots
![WhatsApp Image 2026-03-21 at 07 34 51 (1)](https://github.com/user-attachments/assets/29282cd0-a847-4cd2-8bd3-8ac91669d48f)
![WhatsApp Image 2026-03-21 at 07 34 51 (2)](https://github.com/user-attachments/assets/bab89229-5f56-46ce-8078-923f9661bc1c)
![WhatsApp Image 2026-03-21 at 07 34 51](https://github.com/user-attachments/assets/3e0871c4-66a8-4f0d-bfb2-2024ad8f7220)
<img width="1366" height="768" alt="Screenshot_20260322_231102" src="https://github.com/user-attachments/assets/a2e7d912-71c6-4817-8fbf-fbac5fea8ba9" />
<img width="1366" height="768" alt="Screenshot_20260322_231127" src="https://github.com/user-attachments/assets/bed3483e-4d08-4436-8b95-04cd2d9376c2" />

---

## 🔥 Highlights

- Fully automated DevOps system  
- AI-driven decision making  
- Self-healing infrastructure  
- Zero-cost AI (local LLM)  
- Production-like architecture  

---

## 🧠 Future Improvements

- Slack alerts integration  
- Prometheus monitoring  
- Multi-cluster support  
- Advanced LLM reasoning  
- Incident dashboard  

---

## 👨‍💻 Author

Vaibhav Agarwal


