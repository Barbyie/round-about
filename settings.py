import pickle

map_folder_name = input("Path that your world folder is located:\n")
backup_path_folder = input("Path that the backup folder will be created:\n")
backup_frequency = int(input("Frequency that you want to take backups (in seconds):\n"))

with open('parameters.pk1', 'wb') as file:
    
    pickle.dump((backup_path_folder, map_folder_name, backup_frequency), file)