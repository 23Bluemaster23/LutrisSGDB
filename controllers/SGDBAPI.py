import gi

from models.FileSystem import ImageModel
from utils.CONSTANTS import ImageType,ImageSize,ThumbnailSize
gi.require_version("Gtk", "3.0")
from models.SGDBAPI import SGDBAPIModel
from gi.repository import GLib, GdkPixbuf,Gtk

class SGDBAPIController:
    @staticmethod
    def search_game(query:str):
        res = SGDBAPIModel.search_game(query=query)
        if res['success']:
            header = ['id','name']
            data = res['data']

            formated_data = list(map(lambda item: dict(zip(header,[item['id'],item['name']])),data))

            return formated_data
        
        return {'success':False,'msg':'Game Not Found'}

    @staticmethod
    def fetch_image(id:int,type:str):
        res = SGDBAPIModel.fetch_image(id,type)
        if res['success']:
            header = ['url','thumb']
            data = res['data']

            formated_data = list(map(lambda item: dict(zip(header,[item['url'],item['thumb']])),data))

            return formated_data
        
        return {'success':False,'msg':'Game Not Found'}
    @staticmethod
    def get_url_thumbnail(url:str,type:str):
        image_res = SGDBAPIModel.get_url_image(url=url)
        loader = GdkPixbuf.PixbufLoader()
        match type:
            case ImageType.ICON:
                loader.set_size(ThumbnailSize.ICON['width'],ThumbnailSize.ICON['height'])
            case ImageType.BANNER:
                loader.set_size(ThumbnailSize.BANNER['width'],ThumbnailSize.BANNER['height'])
            case ImageType.COVERART:
                loader.set_size(ThumbnailSize.COVERART['width'],ThumbnailSize.COVERART['height'])
        loader.write_bytes(GLib.Bytes.new(image_res['content']))
        loader.close()

        pifbuf = loader.get_pixbuf()
        image  = Gtk.Image.new_from_pixbuf(pifbuf)
        return image
    @staticmethod
    def get_url_image(url:str,type:str):
        image_res = SGDBAPIModel.get_url_image(url=url)
        loader = GdkPixbuf.PixbufLoader()
        match type:
            case ImageType.ICON:
                loader.set_size(ImageSize.ICON['width'],ImageSize.ICON['height'])
            case ImageType.BANNER:
                loader.set_size(ImageSize.BANNER['width'],ImageSize.BANNER['height'])
            case ImageType.COVERART:
                loader.set_size(ImageSize.COVERART['width'],ImageSize.COVERART['height'])
        loader.write_bytes(GLib.Bytes.new(image_res['content']))
        loader.close()

        pifbuf = loader.get_pixbuf()
        image  = Gtk.Image.new_from_pixbuf(pifbuf)
        return image
    @staticmethod
    def save_image(image:Gtk.Image,slug,type):
        pifbuf = image.get_pixbuf()
        pifbuf.savev(ImageModel.get_image_path_for_save(type=type,slug=slug),ImageModel.get_filetype(type=type))
    
   