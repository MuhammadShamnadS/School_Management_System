import time
import json
import os

AUTH_LOG = "data/auth_log.json"
USERNAME = "admin"
PASSWORD = "admin"
BLOCK_DURATION = 300  
MAX_ATTEMPTS = 3

def load_auth_log():
    if os.path.exists(AUTH_LOG):
        with open(AUTH_LOG, 'r') as f:
            return json.load(f)
    return {"failed_attempts": 0, "last_attempt_time": 0}

def save_auth_log(log_data):
    with open(AUTH_LOG, 'w') as f:
        json.dump(log_data, f)

def authenticate():
    log = load_auth_log()
    current_time = time.time()

    if log["failed_attempts"] >= MAX_ATTEMPTS:
        if current_time - log["last_attempt_time"] < BLOCK_DURATION:
            remaining = int((BLOCK_DURATION - (current_time - log["last_attempt_time"])) / 60)
            print(f"Too many failed attempts. Please try again after {remaining} minute(s).")
            return False
        else:
            log["failed_attempts"] = 0

    while log["failed_attempts"] < MAX_ATTEMPTS:
        username = input("Username: ")
        password = input("Password: ")


        username_correct = username == USERNAME
        password_correct = password == PASSWORD

        if username_correct and password_correct:
            log["failed_attempts"] = 0
            save_auth_log(log)
            print("Login successful.")
            return True
        else:
            log["failed_attempts"] += 1
            log["last_attempt_time"] = current_time
            save_auth_log(log)


            if not username_correct and not password_correct:
                print("Username and password are incorrect.")
            elif not username_correct:
                print("Username is incorrect.")
            else:
                print("Password is incorrect.")


            attempts_left = MAX_ATTEMPTS - log["failed_attempts"]
            if attempts_left > 0:
                print(f"{log['failed_attempts']} attempt(s) failed, {attempts_left} remaining.")
            else:
                print("Maximum attempts reached. Login blocked for 5 minutes.")
                return False

    return False