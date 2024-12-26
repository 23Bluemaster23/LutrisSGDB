import gi
gi.require_version("Gtk", "3.0")
from models.FileSystem import ConfigModel,ImageModel
from gi.repository import GdkPixbuf,Gtk
from utils.CONSTANTS import ImageType,ThumbnailSize
class ConfigController:
    @staticmethod
    def get_config(section:str,key:str):
        return ConfigModel.get_config(section=section,key=key)
    @staticmethod
    def set_config(section:str,key:str,value):
        ConfigModel.set_config(section=section,key=key,value=value)

class ImageController:
    @staticmethod
    def get_image(type:str,slug:str):
        image_path = ImageModel.get_image_path(type=type,slug=slug)
        pifbuf = None
        match type:
            case ImageType.ICON:
                pifbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(image_path,ThumbnailSize.ICON['width'],ThumbnailSize.ICON['height'],True)
            case ImageType.BANNER:
                pifbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(image_path,ThumbnailSize.BANNER['width'],ThumbnailSize.BANNER['height'],True)
            case ImageType.COVERART:
                pifbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(image_path,ThumbnailSize.COVERART['width'],ThumbnailSize.COVERART['height'],True)
        image = Gtk.Image.new_from_pixbuf(pifbuf)
        return image
        
        