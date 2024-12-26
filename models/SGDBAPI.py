
from controllers.FileSystem import ConfigController
from utils.CONSTANTS import ImageType
import requests
import json
headers = {
            'Authorization': 'Bearer ' + ConfigController.get_config('API','api_key')
        }
class SGDBAPIModel:
    @staticmethod
    def search_game(query:str):
        
        url = 'https://www.steamgriddb.com/api/v2/search/autocomplete/{0}'.format(query)
        try:
            res = json.loads(requests.get(url=url,headers=headers).content)
        except:
            res = {"success":False}

        return res
    @staticmethod
    def fetch_image(id:int,type:str):
        url = ""
        match type:
            case ImageType.ICON:
                url = 'https://www.steamgriddb.com/api/v2/icons/game/{0}'.format(id)
            case ImageType.BANNER:
                url = 'https://www.steamgriddb.com/api/v2/grids/game/{0}?dimensions=460x215,920x430'.format(id)
            case ImageType.COVERART:
                url = 'https://www.steamgriddb.com/api/v2/grids/game/{0}?dimensions=600x900'.format(id)
        
        try:
            res = json.loads(requests.get(url=url,headers=headers).content)
        except:
           res = {"success":False}

        return res
    @staticmethod
    def get_url_image(url):
        
        try:
            res =      requests.get(url=url)
            return {"success":True,"content":res.content}
        except:
            return {"success":True,"msg":"Error Loading Image"}