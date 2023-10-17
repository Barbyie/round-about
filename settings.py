import pickle

name_map = input("Map Folder Name:\n")
map_path_folder = input("Path that your world folder is located:\n")
backup_folder_name = input("Backup Folder Name:\n")
backup_path_folder = input("Path that the backup folder will be created:\n")
backup_frequency = input("Frequency that you want to take backups (in seconds):\n")

with open('variables.pk1', 'wb') as file:
    
    pickle.dump((name_map, backup_folder_name, backup_path_folder, map_path_folder, backup_frequency), file)
