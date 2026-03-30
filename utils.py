# utils.py

import time  # Used for delay in real-time monitoring

def follow(file):
    """
    STEP 6: Real-time log monitoring (like 'tail -f')

    WHY?
    - SOC analysts monitor logs continuously
    - This simulates live log ingestion
    """

    file.seek(0, 2)  # Move cursor to end of file

    while True:
        line = file.readline()  # Read new line

        if not line:
            time.sleep(0.5)  # Wait if no new logs
            continue

        yield line  # Return new log line