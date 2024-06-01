import os
from box.exceptions import BoxValueError
import yaml
from WineQPrediction import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import path
from typing import Any
from pathlib import Path



@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    reads yaml file and returns
    
    Args:
        path_to_yaml (Path): Path to yaml file
    
    Raises:
        BoxValueError: If the file is not found
    
    Returns:
        ConfigBox: ConfigBox object
     """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """create list of dictionarires

    Args:
        path_to_directories (list): _description_
        verbose (bool, optional): _description_. Defaults to True.
        ignore_logs (bool, optional): _description_. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory created at {path}")
            
@ensure_annotations
def save_json(path:Path,data:dict):
    """save json data

    Args:
        path (Path): path to json
        data (dict): data to be saved in json file
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
        logger.info(f"Json Data saved at {path}")
    
    
@ensure_annotations
def load_json(pathLPath) -> ConfigBox:
    """load json data

    Args:
        pathLPath ([type]): [description]

    Returns:
        ConfigBox: [description]
    """
    with open(path) as f:
        data = json.load(f)
        logger.info(f"Json Data loaded from {path}")
        return ConfigBox(data)

@ensure_annotations
def save_bin(data:Any,Path:Path):
    """save binary data

    Args:
        data (Any): data to be saved
        Path (Path): path to save data
    """
    with open(Path,"wb") as f:
        joblib.dump(data,f)
        logger.info(f"Binary data saved at {Path}")
        

@ensure_annotations
def load_bin(Path:Path) -> Any:
    """load binary data

    Args:
        Path (Path): path to load data

    Returns:
        Any: data
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from:{path} ")

@ensure_annotations
def get_size(path:Path) -> str:
    """get size of file

    Args:
        path (Path): path to file

    Returns:
        str: size of file
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"