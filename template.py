import os
from pathlib import Path
import logging

ProjectName="TestProject"

List_Files=[
    ".gethub/Workflows/.getkeep",
    f"src/{ProjectName}/__init__.py",
    f"src/{ProjectName}/component/__init__.py",
    f"src/{ProjectName}/constant/__init__.py",
    f"src/{ProjectName}/entity/__init__.py",
    f"src/{ProjectName}/config/__init__.py",
    f"src/{ProjectName}/pipeline/__init__.py",
    f"src/{ProjectName}/utils/__init__.py",
    "config/config.yaml",
    "param.yaml",
    "requirement.txt",
    "setup.py",
    "reserach/trails.ipynb"
]


for filepath in List_Files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory {filedir} successfully")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
             pass
        logging.info(f"Creating file {filename}")
    else:
        logging.info(f"Creating empty file {filepath}")



           


        



        
