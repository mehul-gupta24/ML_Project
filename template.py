
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


project_name="ML_Project"
list_of_files=[
    # ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componnents/__init__.py",
    f"src/{project_name}/componnents/data_ingestion.py",
    f"src/{project_name}/componnents/data_transformation.py",
    f"src/{project_name}/componnents/model_trainer.py",
    f"src/{project_name}/componnents/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/trianing_pipelines.py",
    f"src/{project_name}/pipelines/prediction_pipelines.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/logger.py",
    "app.py",
    "DockerFile",
    "requirements.txt",
    "setup.py",
]

for file_path in list_of_files:
    file_path=Path(file_path)
    file_dir,file_name=os.path.split(file_path)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory : {file_dir} for the file {file_name} ")

    if(not os.path.exists(file_path))or(os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
        logging.info(f"Creating empty file : {file_path}")
    else:
        logging.info(f"{file_name} Already Exists")

