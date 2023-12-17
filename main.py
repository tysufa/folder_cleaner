import os
# import platform


home_files = os.listdir("/home/tysufa") # TODO : pouvoir adapter le dossier a n'importe quel utilisateur

download_files = []

if "Downloads" in home_files:
    download_files = os.listdir("/home/tysufa/Downloads")

if "Téléchargements" in home_files and len(download_files) == 0:
    download_files = os.listdir("/home/tysufa/Téléchargements")

def move_file(file_path, dest_folder): # TODO : ne pas vérifier seulement le dernier fichie/dossier pour voir s'ils existent 
    file_name = file_path.split("/")[-1]
    file_folder = "/".join(file_path.split("/")[:-1])
    dir_folder = "/".join(dest_folder.split("/")[:-1])
    dir_name = dest_folder.split("/")[-1]
    if file_name not in os.listdir(file_folder):
        print("le fichier '" + file_name + "' n'existe pas")
    elif dir_name not in os.listdir(dir_folder):
        print("Le dossier de destination n'existe pas")
    elif file_path.split("/")[-1] in os.listdir(dest_folder):
        print("Le fichier '" + file_name + "' existe deja dans le dossier de destination")
    else:
        os.rename(file_path, dest_folder + "/" + file_path.split("/")[-1])
        print("Le fichier à bien été deplacé") 

tempo_path = os.getcwd() 
move_file(tempo_path + "/test2", tempo_path + "/oui")

if len(download_files) > 0:
    for el in download_files:
        if el.split(".")[-1] == "py":
            pass
        elif el.split(".")[-1] == "cpp":
            pass
        elif el.split(".")[-1] == "c":
            pass
        elif el.split(".")[-1] == "cpp":
            pass
        elif el.split(".")[-1] == "c":
            pass
        elif el.split(".")[-1] == "o":
            pass
        elif el.split(".")[-1] == "backup":
            pass
        elif el.split(".")[-1] == "txt":
            pass
        elif el.split(".")[-1] == "png":
            pass
        elif el.split(".")[-1] == "jpg":
            pass
        elif el.split(".")[-1] == "gif":
            pass
