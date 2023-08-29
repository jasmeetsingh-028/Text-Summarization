#all the logc
import os
from pathlib import Path
import logging   #to log everthing during runtime


#core components
#logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarization"

#required file and folders

list_of_file = [
    ".github/workflows/.gitkeep/",  #for ci/cd
    f"src/{project_name}/__init__.py",   #__init__ constructor file
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "notebooks_and_research/n1.ipynb",
    ]


#logic to create files

for filepath in list_of_file:
    filepath = Path(filepath)  #detects os and makes filepath acoording to it eg windows- WindowsPath(filepath)
    filedir, filename = os.path.split(filepath)  #to split file dir and file path

    #checking if file directory is not empty

    #FOLDER CREATION
    if filedir != "":  #if filedir is not empty
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"creating directory: {filedir} for the file: {filename}")

    #FILE CREATION
    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)): #if file does not exist and file size ==0 then create file
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file: {filepath} ")   #just creating file not writing anything to it
    
    else:
         logging.info(f"{filename} already exists ")