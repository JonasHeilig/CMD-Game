import datetime
import os


class Logger:
    def __init__(self):
        self.log_file = None

    def start_log(self):
        now = datetime.datetime.now()
        log_filename = f"log_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, log_filename)
        self.log_file = open(log_path, 'a')
        self.log_file.flush()

    def log(self, message, prefix):
        if self.log_file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_message = f"{timestamp} [{prefix}] {message}"
            # To Debug
            print(log_message)
            self.log_file.write(log_message + '\n')
            self.log_file.flush()
        else:
            print("Logger has not been started. Please call start_log() first.")

    def log_info(self, message):
        self.log(message, prefix="INFO")

    def log_warning(self, message):
        self.log(message, prefix="WARNING")

    def log_error(self, message):
        self.log(message, prefix="ERROR")

    def log_close_log(self):
        if self.log_file:
            self.log_file.close()
            self.log_file = None
