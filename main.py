import os
import subprocess
import datetime
import sys

class Backup:

    def __init__(self, name, origin=os.path.dirname(__file__) + "/world",
                 destination=os.path.dirname(__file__) + "/thiago"):
        self.name = name
        self.origin = origin
        self.destination = destination

    def trigger(self):
                time_instance = Time()
                try:
                    compress = f"tar -czvf {self.destination}/{self.name}-{time_instance.formatted_time} {self.origin}"
                    compress_exec = subprocess.run(compress, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                               text=True, check=True)
                    print(f"Backup created successfully at {time_instance.formatted_time}")
                except subprocess.CalledProcessError as error_message:
                    print("Backup creation failed with error:\n", error_message.stderr)

    def check_if_destination_folder_exists(self):
        if os.path.exists(self.destination):
            print("Backup folder already exists.")
        else:
            print("Backup folder does not exist yet, creating it.")
            try:
                os.makedirs(self.destination)
                print("Backup folder created successfully.")
            except OSError as error:
                print(f"Failed to create the folder with the error:\n{error}")
                print("Exiting the program.")
                sys.exit(1)

class Time:

    def __init__(self):
        current_time = datetime.datetime.now()
        self.formatted_time = current_time.strftime("%y-%m-%d-%I-%M-%S-%p")


call_backup = Backup(name="thiago", destination="/var/log/test")
call_backup.check_if_destination_folder_exists()
call_backup.trigger()

# create_destination = f"mkdir -p {self.destination}"
# run_create = subprocess.run(create_destination, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# error_message_folder = subprocess.CalledProcessError
