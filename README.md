# 🔐 SIEM Log Monitor

A Python-based **real-time log monitoring and threat detection system** that simulates core SIEM (Security Information and Event Management) functionality used in SOC environments.

---

## 📌 Overview

This project continuously monitors system logs, parses unstructured log data, and detects suspicious activities such as **brute-force login attempts**. It demonstrates how security teams analyze logs and generate alerts in real time.

---

## 🚀 Features

- ✅ Real-time log monitoring (similar to `tail -f`)
- ✅ Log parsing using Regular Expressions (Regex)
- ✅ Brute-force attack detection (rule-based)
- ✅ Automated alert generation
- ✅ Modular and scalable code structure

---

## 🧠 How It Works

Pipeline:
Logs → Parsing → Detection → Alerting

### 🔹 Components

- **Log Parser (`log_parser.py`)**
  - Converts raw logs into structured data (dictionary format)

- **Threat Detector (`detector.py`)**
  - Identifies suspicious activity using rule-based logic

- **Alert System (`alert.py`)**
  - Displays security alerts in real time

- **Real-Time Monitor (`utils.py`)**
  - Continuously reads new log entries (like `tail -f`)

- **Main Pipeline (`main.py`)**
  - Connects all components into a working system

---

## 🛠 Tech Stack

- Python
- Regex
- Collections (defaultdict)

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/anshpdyadav7-blip/siem-log-monitor.git

# Go to project folder
cd siem-log-monitor

# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate

# Run the project
python3 main.py

📄 Sample Log Format
2026-03-30 10:16:10 ERROR Failed login user=admin ip=192.168.1.10
🚨 Sample Output
🚨 SECURITY ALERT 🚨
Type: Brute Force Attack
User: admin
IP: 192.168.1.10
Attempts: 3
📁 Project Structure
siem-log-monitor/
│── logs/
│   └── system.log
│── main.py
│── log_parser.py
│── detector.py
│── alert.py
│── utils.py
│── README.md
🔥 Future Improvements
🌍 IP Geolocation tracking
📧 Email/Slack alert integration
📊 Web dashboard using Flask
🔍 Additional attack detection rules (SSH, port scan, etc.)
📁 Export alerts to JSON/CSV
💡 Learning Outcomes
Understanding SIEM architecture
Log parsing and normalization
Rule-based threat detection
Real-time monitoring systems
Git & GitHub workflow
👨‍💻 Author

Ansh Yadav
GitHub: https://github.com/anshpdyadav7-blip