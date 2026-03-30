# main.py

# STEP 7: Import all modules (pipeline components)
from log_parser import parse_log_line
from detector import detect_threat
from alert import send_alert
from utils import follow

def main():
    """
    MAIN PIPELINE (VERY IMPORTANT)

    Flow:
    Logs → Parse → Detect → Alert

    This is exactly how SIEM systems work.
    """

    # STEP 8: Open log file in read mode
    log_file = open("logs/system.log", "r")

    # STEP 9: Continuously monitor logs
    for line in follow(log_file):

        # STEP 10: Parse raw log into structured data
        parsed_log = parse_log_line(line)

        # Ignore invalid logs
        if not parsed_log:
            continue

        # STEP 11: Detect threats
        alerts = detect_threat(parsed_log)

        # STEP 12: Send alerts if any detected
        for alert in alerts:
            send_alert(alert)

# STEP 13: Entry point of program
if __name__ == "__main__":
    main()