CONFIG_PATH = '~/.config/lutris-sgdb/config.ini'
STYLES_PATH = 'resources/styles.css'
DEFAULT_IMAGE_PATH = 'resources/images/default.png'
class ImageType:
    BANNER = 'banner'
    COVERART = 'coverart'
    ICON = 'icon'
    
class ThumbnailSize:
    BANNER = {'width':184,'height':69}
    COVERART = {'width':132,'height':176}
    ICON = {'width':64,'height':64}
    
class ImageSize:
    BANNER = {'width':368,'height':138}
    COVERART = {'width':528,'height':704}
    ICON = {'width':128,'height':128}