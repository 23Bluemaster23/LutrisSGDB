import gi
import threading
gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk
from controllers.SGDBAPI import SGDBAPIController
class SearchWindow(Gtk.Builder):
    def __init__(self,name,type):
        super().__init__()
        self.success = False
        self.type = type
        self.selected_id = 0
        self.add_from_file('templates/SearchWindow.glade')
        
        self.window:Gtk.Window = self.get_object('SearchWindow')
        
        self.search_entry :Gtk.Entry= self.get_object('search_entry')
        self.search_entry.set_text(name)
        
        self.search_Button:Gtk.Button = self.get_object('search_btn')
        self.search_Button.connect('clicked',self.on_search_button_pressed)
        self.loading_box:Gtk.Box = self.get_object('loading_box')
        
        self.result_box: Gtk.Box = self.get_object('result_box')
    
    def update_search_box(self):
        GLib.idle_add(self.clear_result_box)
        GLib.idle_add(self.show_loading)
        data_list = SGDBAPIController.search_game(self.search_entry.get_text())
        
        for item in data_list:
            GLib.idle_add(self.create_search_box,item)
        GLib.idle_add(self.hide_loading)
    def clear_result_box(self):
        for child in self.result_box.get_children():
            child.destroy()
    def create_search_box(self,item):
        sb = SearchBox()
        sb.set_game_data(item)
        sb.edit_button.connect('clicked',self.on_select_button_pressed,item['id'])
        self.result_box.pack_start(sb,False,True,4) 
        sb.show_all()   
    def on_search_button_pressed(self,widget):
        th = threading.Thread(target=self.update_search_box)
        th.daemon = True
        th.start()
    def on_select_button_pressed(self,widget,id):
        self.selected_id = id
        self.success = True
        self.window.close()
    def show_loading(self):
        self.loading_box.show()
    def hide_loading(self):
        self.loading_box.hide()
class SearchBox(Gtk.Box):
    def __init__(self,**kargs):
        super().__init__(**kargs,orientation=Gtk.Orientation.HORIZONTAL,margin_start=5,margin_end=5)
        self.info_box:Gtk.Box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,margin_start=5,margin_end=5,margin_top=5,margin_bottom=5,spacing=5)
        self.info_box.set_hexpand(True)
        
        self.add(self.info_box)
        self.set_name('game_box')

        self.name_label:Gtk.Label = Gtk.Label(label='Name',justify=Gtk.Justification.LEFT,halign=Gtk.Align.START)
        self.info_box.pack_start(self.name_label,True,True,0)
        

        self.id_label:Gtk.Label = Gtk.Label(label='Slug',justify=Gtk.Justification.LEFT,halign=Gtk.Align.START)
        self.info_box.pack_start(self.id_label,True,True,0)

        self.edit_button:Gtk.Button = Gtk.Button(label='edit',valign=Gtk.Align.CENTER)
        self.pack_start(self.edit_button,False,False,0)
        
        
    def set_game_data(self,data:dict)->None:
        self.name_label.set_text(data['name'])
        self.id_label.set_text(str(data['id']))
    
    