import os
import subprocess
import datetime
import sys
import logging
import signal
import time
import pickle


map_folder_name = None
backup_folder_name = None

try:
    with open('parameters.pk1', 'rb') as file:
        backup_path_folder, map_folder_name, backup_frequency = pickle.load(file)
except FileNotFoundError:
    backup_path_folder = None
    map_folder_name = None
    backup_frequency = None
#It will try to open the parameters and in case it does not find the file, initiates the variables with None.

class Backup:

    def __init__(self, name, origin=map_folder_name, destination=backup_path_folder):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.log = Logs()
    def trigger(self):
                time_instance = Time()
                try:
                    compress = f"tar -czvf {self.destination}/{self.name}-{time_instance.formatted_time} {self.origin}"
                    compress_exec = subprocess.run(compress, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                               text=True, check=True)
                    print(f"Backup created successfully at {time_instance.formatted_time}")
                    self.log.create_logs(f"Backup created successfully at {time_instance.formatted_time}")
                except subprocess.CalledProcessError as error_message:
                    print("Backup creation failed with error:\n", error_message.stderr)
                    self.log.create_logs("Backup creation failed with error:\n", error_message.stderr)
    def check_if_destination_folder_exists(self):
        if os.path.exists(self.destination):
            print("Backup folder already exists.")
            self.log.create_logs("Backup folder already exists.")
        else:
            print("Backup folder does not exist yet, creating it.")
            self.log.create_logs("Backup folder does not exist, creating it.")
            try:
                os.makedirs(self.destination)
                print("Backup folder created successfully.")
                self.log.create_logs("Backup folder created successfully.")
            except OSError as error:
                print(f"Failed to create the folder with the error:\n{error}")
                self.log.create_logs(f"Failed to create the folder with the error:\n{error}")
                print("Exiting the program.")
                self.log.create_logs("Exiting the program.")
                sys.exit(1)

class Time:

    def __init__(self):
        current_time = datetime.datetime.now()
        self.formatted_time = current_time.strftime("%y-%m-%d-%I-%M-%S-%p")

class Logs:

    def create_logs(self, log_message):
        log_folder = os.path.dirname(os.path.abspath(__file__))
        log_file = "round-about.log"
        logging.basicConfig(filename=os.path.join(log_folder, log_file), level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger(__name__)
        logger.debug(log_message)

class SignalReceiver:

    def __init__(self):
        signal.signal(signal.SIGTERM, self.sigterm_handler)
        signal.signal(signal.SIGINT, self.sigterm_handler)
    def sigterm_handler(self, signum, frame):
        self.log = Logs()
        print("Received EXIT signal. Exiting the program.")
        self.log.create_logs("Received EXIT signal. Exiting the program.")
        sys.exit(0)

signal_detector = SignalReceiver()

call_backup = Backup(name="roundabout")
call_backup.check_if_destination_folder_exists()
while True:
    call_backup.trigger()
    time.sleep(backup_frequency)



