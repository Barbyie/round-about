import os
import subprocess
import datetime

map_name = "world"
backupfolder_name = "roundabout-backups"
#This variable defines the name of the Map and the Backup Folder.

script_directory = os.path.dirname(os.path.abspath(__file__))
#This variable checks the Absolute path of the script.

map_path = os.path.join(script_directory, map_name)
backup_path = os.path.join(script_directory, backupfolder_name)
#This variable is used to set the directory of the Map and the Backup Folder.


def createBackup():

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%y-%m-%d-%I-%M-%p")
    #current_time will get the current time and formatted_time will format the time in YY-MM-DD-HH-MM-AM/PM.
    compress_map = "zip -rX {backup_path}/world-{formatted_time}.zip {map_path}".format(backup_path=backup_path,formatted_time=formatted_time, map_path=map_path)
    compress_exec = subprocess.run(compress_map, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #compress_map creates the command that will be executed, and compress_exec runs the command.

    if compress_exec.returncode == 0:
        return 0
    




    

