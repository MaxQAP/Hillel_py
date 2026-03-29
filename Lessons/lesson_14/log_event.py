import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, 'login_system.log')


def log_event(username: str, status: str):

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    if status == "success":
        level = "INFO"
    elif status == "expired":
        level = "WARNING"
    else:
        level = "ERROR"

    log_message = f"{timestamp} - Login event - Username: {username}, Status: {status} - {level}\n"


    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(log_message)
        f.flush()
        os.fsync(f.fileno())