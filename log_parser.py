# log_parser.py

import re  # Import regex module for pattern matching

def parse_log_line(line):
    """
    STEP 1: Parse raw log line into structured data

    WHY?
    - Logs are unstructured text
    - SIEM tools convert them into structured format (JSON/dict)
    """

    # Regex pattern to extract important fields
    # Example log:
    # 2026-03-30 10:16:10 ERROR Failed login user=admin ip=192.168.1.10
    pattern = r'(\d+-\d+-\d+ \d+:\d+:\d+) (\w+) (.+?) user=(\w+) ip=([\d.]+)'

    # Try matching the pattern
    match = re.search(pattern, line)

    # If match found → convert into dictionary
    if match:
        return {
            "timestamp": match.group(1),  # Extract timestamp
            "level": match.group(2),      # INFO / ERROR
            "message": match.group(3),    # Log message
            "user": match.group(4),       # Username
            "ip": match.group(5)          # IP address
        }

    # If log doesn't match format → ignore
    return None