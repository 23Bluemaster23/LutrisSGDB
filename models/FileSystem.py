
from pathlib import Path
from utils.CONSTANTS import CONFIG_PATH,ImageType,DEFAULT_IMAGE_PATH
from configparser import ConfigParser

if Path(CONFIG_PATH).is_file():
    config = ConfigParser()
    config.read(CONFIG_PATH)
    

class ConfigModel:
    @staticmethod
    def get_config(section:str,key:str):
        return config.get(section=section,option=key)
    @staticmethod
    def set_config(section:str,key:str,value):
        config.set(section=section,option=key,value=value)

class ImageModel:
    @staticmethod
    def get_image_path(type:str,slug:str):
        if type == ImageType.ICON:
            path = Path(config.get('PATHS',type)).joinpath('lutris_'+slug+'.png')
        else:
            path =  Path(config.get('PATHS',type)).joinpath(slug+'.jpg')
        if path.exists():
            return str(path)
        return str(DEFAULT_IMAGE_PATH)
    @staticmethod
    def get_image_path_for_save(type:str,slug:str):
        if type == ImageType.ICON:
            path = Path(config.get('PATHS',type)).joinpath('lutris_'+slug+'.png')
        else:
            path =  Path(config.get('PATHS',type)).joinpath(slug+'.jpg')
        
        return str(path)
    @staticmethod
    def get_filetype(type:str):
        return 'png' if type == ImageType.ICON else 'jpeg'
    