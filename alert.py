# alert.py

def send_alert(alert):
    """
    STEP 5: Handle alerting

    In real-world:
    - Send to SIEM dashboard
    - Send email / Slack / SOC alert system
    """

    print("\n🚨 SECURITY ALERT 🚨")

    # Print alert details clearly
    print(f"Type: {alert['type']}")
    print(f"User: {alert['user']}")
    print(f"IP: {alert['ip']}")
    print(f"Attempts: {alert['count']}")

    print("-" * 40)  # Separator for readability