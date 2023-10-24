import os
import subprocess
import datetime
import signal
import time
import sys
import pickle
import logging

log_folder = os.path.dirname(os.path.abspath(__file__))
log_file = "round-about.log"
#These variables set the folder and the name of the log file.

logging.basicConfig(filename=os.path.join(log_folder, log_file), level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
# The basicConfig sets the filename, the level of the log, and the format which will be displayed.


try:
    with open('variables.pk1', 'rb') as file:
        name_map, backup_folder_name, backup_path_folder, map_path_folder, backup_frequency = pickle.load(file)
        #This will open the variables.pk1 file and grab the arguments that are inside.

except FileNotFoundError:
    
    name_map = None
    map_path_folder = None
    backup_folder_name = None
    backup_path_folder = None
    backup_frequency = None
    #In case these files are not found, all variables will be empty.

complete_backup_path = f"{backup_path_folder}{backup_folder_name}"

#This variable defines the complete path of the Backup Folder.

def sigterm_handler(signum, frame):
    
    print("Received EXIT signal. Exiting the program.")
    logger.debug("Received EXIT signal. Exiting the program.")
    sys.exit(0)
    #This function detects that signal number (in this case SIGTERM) and stops the program when called.

signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigterm_handler)
#When the SIGTERM or SIGINT is sent, it will call the function sigterm_handler, and exit the program.

def createBackup():


    while True:

        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%y-%m-%d-%I-%M-%S-%p")
        #current_time will get the current time and formatted_time will format the time in YY-MM-DD-HH-MM-SS-AM/PM.

        compress_map = f"zip -rX {complete_backup_path}/{name_map}-{formatted_time} {map_path_folder}"
        
        try:

            compress_exec = subprocess.run(compress_map, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            print("Backup created successfully at " + formatted_time)
            logger.debug("Backup created successfully at " + formatted_time)

        except subprocess.CalledProcessError as error_message:

            print("Backup creating failed with error:\n", error_message.stdout)
            logger.debug("Backup creating failed with error:\n", error_message.stdout)
            sys.exit(1)
        #compress_map creates the command that will be executed, and compress_exec runs the command.
        #If the command throws an error, it will display it with the subprocess.CalledProcessError.

        time.sleep(backup_frequency)



if os.path.exists(complete_backup_path):
  
    createBackup()
    # If the Backup folder already exists, it will create the backup.
else:
   
    print("Backup folder does not exist yet, creating it.")
    logger.debug("Backup folder does not exist yet, creating it.")
    create_directory_command = "mkdir " + backup_folder_name
    create_directory = subprocess.run(create_directory_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # If the Backup folder does not exist, it will try to create one before running the backup.

    if create_directory.returncode == 0:
        
        print("Backup folder created successfully.")
        logger.debug("Backup folder created successfully.")
        createBackup()
    
    else:

        print("Failed to create the folder, ending the program.")
        logger.debug("Failed to create the folder, ending the program.")
        sys.exit(1)
        #This will force the program to stop in case the folder is not able to be created.


        
    




    

