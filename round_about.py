import os
import subprocess
import datetime
import time
import sys
import pickle

try:
    with open('variables.pk1', 'rb') as file:
        name_map, backup_folder_name = pickle.load(file)
        #This will open the variables.pk1 file and grab the arguments that are inside.

except FileNotFoundError:
    name_map = None
    backup_folder_name = None
    #In case the file is not found, both variables will be empty.

map_name = name_map
backupfolder_name = backup_folder_name
#This variable defines the name of the Map and the Backup Folder.

script_directory = os.path.dirname(os.path.abspath(__file__))
#This variable checks the Absolute path of the script.

map_path = os.path.join(script_directory, map_name)
backup_path = os.path.join(script_directory, backupfolder_name)
#This variable is used to set the directory of the Map and the Backup Folder.


def createBackup():

    time_running = 300
    #Every X time another backup will be generated.

    while True:

        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%y-%m-%d-%I-%M-%S-%p")
        #current_time will get the current time and formatted_time will format the time in YY-MM-DD-HH-MM-SS-AM/PM.

        compress_map = "zip -rX {backup_path}/{map_name}-{formatted_time}.zip {map_path}".format(backup_path=backup_path,formatted_time=formatted_time, map_path=map_path, map_name=map_name)
        
        try:

            compress_exec = subprocess.run(compress_map, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            print("Backup created successfully at " + formatted_time)

        except subprocess.CalledProcessError as error_message:

            print("Backup creating failed with error:\n", error_message.stdout)
            sys.exit(1)
        #compress_map creates the command that will be executed, and compress_exec runs the command.
        #If the command throws an error, it will display it with the subprocess.CalledProcessError.

        time.sleep(time_running)

if os.path.exists(backup_path):
  
    createBackup()
    # If the Backup folder already exists, it will create the backup.
else:
   
    print("Backup folder does not exist yet, creating it...")
    create_directory_command = "mkdir " + backup_path
    create_directory = subprocess.run(create_directory_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # If the Backup folder does not exist, it will try to create one before running the backup.

    if create_directory.returncode == 0:
        
        print("Backup folder created successfully.")
        createBackup()
    
    else:

        print("Failed to create the folder, ending the program.")
        sys.exit(1)
        #This will force the program to stop in case the folder is not able to be created.


        
    




    

