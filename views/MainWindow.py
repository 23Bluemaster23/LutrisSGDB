import gi

from views.ConfigWindow import ConfigWindow
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from controllers.SqliteDb import SqliteDbController
from .GameWindow import GameWindow
class MainWindow(Gtk.Builder):
    
    def __init__(self, **kargs):
        super().__init__(**kargs)
    
        self.add_from_file('templates/MainWindow.glade')
        self.main_window:Gtk.ApplicationWindow = self.get_object(name='MainWindow')
        self.main_window
        self.games_box:Gtk.Box = self.get_object(name='game_box')
        self.setting_action = self.get_object('setting_action')
        self.setting_action.connect('activate',self.open_settings_window)
        self.update_game_box()
        self.games_box.set_name('game_box')
    def update_game_box(self):
        res = SqliteDbController.get_all_games()
        for item in res:
            gb = GameBox(self.main_window)
            gb.set_game_data(item)
            self.games_box.pack_start(gb,False,False,0)
    def open_settings_window(self,widget):
        wind = ConfigWindow()
        wind.window.set_modal(True)
        wind.window.set_transient_for(self.main_window)
        wind.window.show()
class GameBox(Gtk.Box):
    def __init__(self,parent,**kargs):
        super().__init__(**kargs,orientation=Gtk.Orientation.HORIZONTAL,margin_start=5,margin_end=5)
        self.parent:Gtk.Window = parent
        
        self.info_box:Gtk.Box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,margin_start=5,margin_end=5,margin_top=5,margin_bottom=5,spacing=5)
        self.info_box.set_hexpand(True)
        self.add(self.info_box)
        self.set_name('game_entry')

        self.name_label:Gtk.Label = Gtk.Label(label='Name',justify=Gtk.Justification.LEFT,halign=Gtk.Align.START)
        self.info_box.pack_start(self.name_label,True,True,0)

        
        self.slug_label:Gtk.Label = Gtk.Label(label='Slug',justify=Gtk.Justification.LEFT,halign=Gtk.Align.START)
        self.info_box.pack_start(self.slug_label,True,True,0)

        self.platform_label:Gtk.Label = Gtk.Label(label='Platform',justify=Gtk.Justification.LEFT,halign=Gtk.Align.START)
        self.info_box.pack_start(self.platform_label,True,True,0)

        self.edit_button:Gtk.Button = Gtk.Button(label='edit',margin_start=2,margin_end=5,valign=Gtk.Align.CENTER)
        self.edit_button.connect('clicked',self.open_game_window)
        self.pack_start(self.edit_button,False,False,0)
    
    def set_game_data(self,data:dict)->None:
        self.name_label.set_text(data['name'])
        self.slug_label.set_text(data['slug'])
        self.platform_label.set_text(data['platform'])
    
    def open_game_window(self,widget):
        gw = GameWindow(self.name_label.get_text(),self.slug_label.get_text())
        gw.window.present()
        gw.window.set_modal(True)
        gw.window.set_transient_for(self.parent)
        gw.window.show_all()