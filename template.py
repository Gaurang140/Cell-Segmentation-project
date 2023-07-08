import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='[%(asctime)s] %(message)s:')

project = "cellSengmentationYolo"


list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project}/__init__.py",
    f"{project}/components/__init__.py",
    f"{project}/components/data_ingestion.py",
    f"{project}/components/data_validation.py",
    f"{project}/components/model_trainer.py",
    f"{project}/constant/__init__.py",
    f"{project}/constant/training_pipeline/__init__.py",
    f"{project}/constant/application.py",
    f"{project}/entity/config_entity.py",
    f"{project}/entity/artifacts_entity.py",
    f"{project}/exception/__init__.py",
    f"{project}/logger/__init__.py",
    f"{project}/pipeline/__init__.py",
    f"{project}/pipeline/training_pipeline.py",
    f"{project}/utils/__init__.py",
    f"{project}/utils/main_utils.py",
    "research/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]


for file in list_of_files:
    file = Path(file)

    filedir , filename = os.path.split(file)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory:{filedir} for the file name {filename}")

    if(not os.path.exists(filename))or (os.path.getatime(filename)==0):
        with open(file, 'w') as f:
            pass 
            logging.info(f"Created empty file: {filename}")
    else:
        logging.info(f"{filename} is already exists")

