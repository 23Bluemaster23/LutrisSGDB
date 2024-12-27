import gi

from controllers.SGDBAPI import SGDBAPIController
from views.Dialogs import CompletedDialog
from views.FetchWindow import FetchWindow
from views.SearchWindow import SearchWindow
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from utils.CONSTANTS import ImageType
from controllers.FileSystem import ImageController
class GameWindow(Gtk.Builder):
    def __init__(self,name,slug):
        super().__init__()
        
        self.add_from_file('templates/GameWindow.glade')
        self.window = self.get_object('GameWindow')
        

        self.name_label:Gtk.Label= self.get_object(name='name_label')
        self.name_label.set_text(name)

        self.slug_label:Gtk.Label = self.get_object(name='slug_label')
        self.slug_label.set_text(slug)

        self.banner_btn:Gtk.Button = self.get_object(name='banner_btn')
        self.banner_btn.connect('clicked',self.open_search_window,ImageType.BANNER)
        self.banner_btn.set_image(ImageController.get_image(ImageType.BANNER,slug))

        self.coverart_btn:Gtk.Button = self.get_object(name='coverart_btn')
        self.coverart_btn.connect('clicked',self.open_search_window,ImageType.COVERART)
        self.coverart_btn.set_image(ImageController.get_image(ImageType.COVERART,slug))
        
        self.icon_btn:Gtk.Button = self.get_object(name='icon_btn')
        self.icon_btn.connect('clicked',self.open_search_window,ImageType.ICON)
        self.icon_btn.set_image(ImageController.get_image(ImageType.ICON,slug))

    def open_search_window(self,widget,type):
        sw = SearchWindow(self.name_label.get_text(),type=type)
        
        sw.window.connect('delete-event',self.open_fetching_window,sw)
        sw.window.present()
        sw.window.set_modal(True)
        sw.window.set_transient_for(self.window)
        sw.window.show_all()
        sw.loading_box.hide()
    def open_fetching_window(self,widget,event,parent):
        if parent.success:
            fw = FetchWindow(parent.selected_id,parent.type)
            fw.window.connect('delete-event',self.save_image,fw)
            fw.window.present()
            fw.window.set_modal(True)
            fw.window.set_transient_for(self.window)
            fw.window.show_all()
            fw.loading_box.hide()
    def update_images(self):
        self.banner_btn.set_image(ImageController.get_image(ImageType.BANNER,self.slug_label.get_text()))
        self.coverart_btn.set_image(ImageController.get_image(ImageType.COVERART,self.slug_label.get_text()))
        self.icon_btn.set_image(ImageController.get_image(ImageType.ICON,self.slug_label.get_text()))
    def save_image(self,widget,event,parent):
        if parent.success:
            SGDBAPIController.save_image(parent.selected_url,type=parent.type,slug=self.slug_label.get_text())
            dg = CompletedDialog()
            dg.dialog.show_all()
            response = dg.dialog.run()
            dg.dialog.destroy()
            self.update_images()