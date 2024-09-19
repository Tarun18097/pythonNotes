# write a program that takes address from user and return a list of file in the directory in that list. 

import os
import shutil

def list_folders(path):
    list_of_files = os.listdir(path)
    print(f"Files in this path: '{path}': {list_of_files}\n")




# based on extensions we have to organize files

def organize_files(address):
    # get list of all files in that dir

    # path_of_folder = input('Enter path of folder where you want to organize files: ')
    path_of_folder = address

    destination_folder = {
        ".jpg": f"{path_of_folder}/Images",
        ".png": f"{path_of_folder}/Images",
        ".mkv": f"{path_of_folder}/Videos",
        ".mp4": f"{path_of_folder}/Videos",
        ".mp3": f"{path_of_folder}/Music",
        ".oog": f"{path_of_folder}/Music",
        ".txt": f"{path_of_folder}/Documents",
        ".docs": f"{path_of_folder}/Documents",
        ".pdf": f"{path_of_folder}/Documents",
        ".odt": f"{path_of_folder}/Documents",
        ".py": f"{path_of_folder}"
    }

    all_files = os.listdir(path_of_folder)

    # loop through each file and check if its a file or not

    for file in all_files:
        file_path = os.path.join(path_of_folder,file)

        if(os.path.isfile(file_path)):
            # get extension of that file
            file_ext = os.path.splitext(file)[1].lower()
            # if this ext exists in destination_folder then add the file into its respective folder

            if(file_ext == '.py'): # skipping py files as its in the correct location.
                continue

            if(file_ext in destination_folder):
                destination = destination_folder[file_ext]
            else:
                # if extension is not present in destination_folder then move file into misc folder.
                destination = f"{path_of_folder}/Misc"

            # move the file
            shutil.move(file_path, os.path.join(destination,file))
            print(f"successfully moved {file} at {destination}")

        else:
            print(f"{file} is not a file.")



# create a folder in the user specified place
def create_dir_structure(address):

    # add = input("Enter file path: : ")
    add = address # did this for gui app.
    
    list_folders(add)

    folders = "Images, Videos, Documents, Music, Misc ".split(",") # returns a list folders = [images, docs, videos]
    folders = [folder.strip() for folder in folders] 
    for folder in folders:
        folder_path = os.path.join(add,folder)  
        if(folder in os.listdir(add)):
            print(f"{folder} already present !")
        else:
            print(f"creating folder {folder}")
            os.makedirs(folder_path)
            print(f"folder created at path {folder_path}")

    organize_files(add)

            # cmd = f"mkdir {folder}"
            # os.system(cmd)

# create_dir_structure()









    

 