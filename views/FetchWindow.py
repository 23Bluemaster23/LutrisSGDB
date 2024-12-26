import gi
import threading

from controllers.SGDBAPI import SGDBAPIController
gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk

class FetchWindow(Gtk.Builder):
    def __init__(self,id,type):
        self.success = False
        super().__init__()
        self.id =id
        self.type = type
        self.selected_url = None
        self.add_from_file('templates/FetchingWindow.glade')
        self.window:Gtk.Window = self.get_object('FetchWindow')
        self.loading_box:Gtk.Box = self.get_object('loading_box')
        self.image_flowbox:Gtk.FlowBox = self.get_object('image_flowbox')
        self.on_open_fetch_window()
    
    def update_flowbox(self):
        GLib.idle_add(self.show_loading)
        res = SGDBAPIController.fetch_image(self.id,type=self.type)
        
        for child in self.image_flowbox.get_children():
            child.destroy()
        image_list = []
        for item in res:
            image_list.append({"url":item['url'],"image":SGDBAPIController.get_url_image(item['thumb'],type=self.type,mode='thumb')})
        GLib.idle_add(self.hide_loading)
        for image in image_list:
            GLib.idle_add(self.create_image_button,image)
    def create_image_button(self,item):
        image =  ImageButton(data=item)
        image.connect('clicked',self.on_image_pressed_button)
        self.image_flowbox.add(image)
        image.show_all()
    def on_open_fetch_window(self):
        th = threading.Thread(target=self.update_flowbox)
        th.daemon = True
        th.start()
    
    def on_image_pressed_button(self,widget):
            self.selected_url = widget.url
            self.success = True
            self.window.close()
    
    def show_loading(self):
        self.loading_box.show()
        
    def hide_loading(self):
        self.loading_box.hide()
class ImageButton(Gtk.Button):
    def __init__(self,data):
        super().__init__(halign=Gtk.Align.CENTER,valign=Gtk.Align.CENTER)
        self.url = data['url']
        self.set_image(data['image'])