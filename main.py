import os
import filetype
# import platform


home_files = os.listdir("/home/tysufa") # TODO : pouvoir adapter le dossier a n'importe quel utilisateur

download_files = []
download_folder_path = ""

if "Downloads" in home_files:
    download_folder_path  = "/home/tysufa/Downloads"
    download_files = os.listdir("/home/tysufa/Downloads")

if "Téléchargements" in home_files and len(download_files) == 0:
    download_folder_path  = "/home/tysufa/Téléchargements"
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
        print("Le fichier '" + file_name + "' à bien été deplacé") 

files_new_folders = { # TODO : gérer dossier francais et anglais et ne pas tenir compte de la casse
    "Images" : "/home/tysufa/Images",
    "Documents" : "/home/tysufa/Documents",
    "Videos" : "/home/tysufa/Videos",
    "Musiques" : "/home/tysufa/Musiques",
    "Programmation" : "/home/tysufa/programmation",
    "Archives" : "/home/tysufa/Archives", # TODO : faire le même programme pour le dossier archives
}

files_extensions = {
    "Images" : ["png", "jpg", "gif"],
    "Documents" : ["txt", "pdf", "docx", "doc", "odt", "ods", "xlsx", "xls"],
    "Videos" : ["mp4", "avi", "mkv"],
    "Musiques" : ["mp3", "wav"],
    "Programmation" : ["py", "cpp", "c", "o", "sql"],
    "Archives" : ["zip", "rar", "tar", "gz", "7z", "xz", "bz2"],
}


if len(download_files) > 0: #TODO : gérer les fichiers sans extension
    for el in download_files:
        extension = el.split(".")[-1]
        if not os.path.isdir(download_folder_path + "/" + el):
            kind = filetype.guess(download_folder_path + "/" + el)
            if kind is not None:
                extension = kind.extension
        print(extension)
        if extension in files_extensions["Images"]:
            if extension == "gif":
                if "gif" not in os.listdir(files_new_folders["Images"]):
                    os.mkdir(files_new_folders["Images"] + "/gif")
                move_file(download_folder_path + "/" + el, files_new_folders["Images"] + "/gif")
            else:
                move_file(download_folder_path + "/" + el, files_new_folders["Images"])

        elif extension in files_extensions["Programmation"]:
            if extension == "py":
                if "downloads" not in os.listdir(files_new_folders["Programmation"] + "/python"):
                    os.mkdir(files_new_folders["Programmation"] + "/python" + "/downloads")
                move_file(download_folder_path + "/" + el, files_new_folders["Programmation"] + "/python" + "/downloads")
            elif extension == "cpp":
                if "downloads" not in os.listdir(files_new_folders["Programmation"] + "/cpp"):
                    os.mkdir(files_new_folders["Programmation"] + "/cpp" + "/downloads")
                move_file(download_folder_path + "/" + el, files_new_folders["Programmation"] + "/cpp" + "/downloads")
            elif extension == "sql":
                if "downloads" not in os.listdir(files_new_folders["Programmation"] + "/sql"):
                    os.mkdir(files_new_folders["Programmation"] + "/sql" + "/downloads")
                move_file(download_folder_path + "/" + el, files_new_folders["Programmation"] + "/sql" + "/downloads")
        elif extension in files_extensions["Documents"]:
            if "downloads" not in os.listdir(files_new_folders["Documents"]):
                os.mkdir(files_new_folders["Documents"] + "/downloads")
            move_file(download_folder_path + "/" + el, files_new_folders["Documents"] + "/downloads")

        elif extension in files_extensions["Videos"]:
            if "Videos" not in home_files:
                os.mkdir(files_new_folders["Videos"])
            if "downloads" not in os.listdir(files_new_folders["Videos"]):
                os.mkdir(files_new_folders["Videos"] + "/downloads")
            move_file(download_folder_path + "/" + el, files_new_folders["Videos"] + "/downloads")

        elif extension in files_extensions["Archives"]:
            if "downloads" not in os.listdir(files_new_folders["Archives"]):
                os.mkdir(files_new_folders["Archives"] + "/downloads")
            move_file(download_folder_path + "/" + el, files_new_folders["Archives"] + "/downloads")
