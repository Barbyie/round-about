import pickle

name_map = input("Map Folder:\n")
backup_folder_name = input("Backup Folder:\n")

with open('variables.pk1', 'wb') as file:
    pickle.dump((name_map, backup_folder_name), file)
