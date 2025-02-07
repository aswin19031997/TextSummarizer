#importing the libraries
import os
from pathlib import Path
import logging

#Creating basic folder template in pythonic way
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')


#Specify project Name
project_name= "textSummarizer"


#List of files 
#common.py will contain components and rest of the constructor are used to import those in other folder
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
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
    "research/trials.ipynb"

]

#Creating above files using the below function or loop
for filepath in list_of_files:
    filepath= Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        #Creation of Folder if File Diretory is not empty
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file {filename}")

    if (not(os.path.exists(filepath))) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating Empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")