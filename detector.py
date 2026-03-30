# detector.py

from collections import defaultdict  # Helps count events easily

# STEP 2: Store failed login attempts globally
# WHY? We need memory to track repeated attempts
failed_attempts = defaultdict(int)

def detect_threat(log):
    """
    Detect suspicious behavior (rule-based detection)

    SOC Concept:
    - This mimics SIEM detection rules (like Sigma rules)
    """

    alerts = []  # Store detected threats

    # STEP 3: Check if log indicates failed login
    if "Failed login" in log["message"]:

        # Create unique key (user + IP)
        key = (log["user"], log["ip"])

        # Increase failed attempt count
        failed_attempts[key] += 1

        # STEP 4: Apply threshold logic
        # If 3 or more failed attempts → possible brute-force attack
        if failed_attempts[key] >= 3:

            alerts.append({
                "type": "Brute Force Attack",
                "user": log["user"],
                "ip": log["ip"],
                "count": failed_attempts[key]
            })

    return alerts