
from pathlib import Path
from utils.CONSTANTS import CONFIG_PATH,ImageType,DEFAULT_IMAGE_PATH
from configparser import ConfigParser

def get_parser(path:Path):
    config_path = path
    config = ConfigParser()
    if config_path.is_file():
        config.read(config_path)
    else:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config['PATHS']  = {
            'db': '~/.local/share/lutris/pga.db',
            'banner' : '~/.local/share/lutris/banners',
            'coverart' : '~/.local/share/lutris/coverart',
            'icon' : '~/.local/share/icons/hicolor/128x128/apps'
        }
        config['API'] = {
            'api_key' : 'your api here'
        }
        with open(config_path,'w') as config_file:
            config.write(config_file)
    return config
config_path = Path(CONFIG_PATH).expanduser()
config = get_parser(config_path)
    

class ConfigModel:
    @staticmethod
    def get_config(section:str,key:str):
        return config.get(section=section,option=key)
    @staticmethod
    def set_config(section:str,key:str,value):
        config.set(section=section,option=key,value=value)
    @staticmethod
    def save_config():
        with open(config_path,'w') as config_file:
            config.write(config_file)

class ImageModel:
    @staticmethod
    def get_image_path(type:str,slug:str,save:bool = False):
        if type == ImageType.ICON:
            path = Path(config.get('PATHS',type)).joinpath('lutris_'+slug+'.png')
        else:
            path =  Path(config.get('PATHS',type)).joinpath(slug+'.jpg')
        if path.expanduser().exists() or save == True:
            
            return str(path.expanduser())
        return str(DEFAULT_IMAGE_PATH)
    @staticmethod
    def get_filetype(type:str):
        return 'png' if type == ImageType.ICON else 'jpeg'
    