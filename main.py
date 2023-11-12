import os
import subprocess
import datetime




class Backup:

    def __init__(self, name, time, origin=os.path.dirname(__file__)+"/world", destination=os.path.dirname(__file__)+"/roundabout"):
        self.name = name
        self.time = time
        self.origin = origin
        self.destination = destination
    
    def trigger(self):        
            command = subprocess.run()

class Time:

    def __str__(self):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%y-%m-%d-%I-%M-%S-%p")
        return formatted_time
        #current_time will get the current time and formatted_time will format the time in YY-MM-DD-HH-MM-SS-AM/PM.

class Compress:

    def __str__(self):
        compress = f"tar -czvf {Backup.destination}/{Backup.name}-{Time()} {Backup.origin}"
        return compress

class Map:

    def __init__(self, name, path):
        self.name = name
        self.path = path


class Log:

    def __init__(self, message, time):
        self.message = message
        self.time = time