import os
import subprocess
import datetime


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



class Time:

    def __init__(self):
        current_time = datetime.datetime.now()
        self.formatted_time = current_time.strftime("%y-%m-%d-%I-%M-%S-%p")

call_backup = Backup(name="thiago")
call_backup.trigger()

