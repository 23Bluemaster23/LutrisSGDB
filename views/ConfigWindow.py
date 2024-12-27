import gi

from controllers.FileSystem import ConfigController
from views.Dialogs import SelectFileDialog, SelectFolderDialog
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ConfigWindow(Gtk.Builder):
    def __init__(self) -> None:
        super().__init__()
        self.add_from_file('templates/OptionsWindow.glade')
        self.window:Gtk.Window = self.get_object('OptionsWindow')
        self.api_entry:Gtk.Entry = self.get_object('api_entry')
        self.api_entry.connect('changed',self.activate_save_button)
        self.db_entry:Gtk.Entry = self.get_object('db_entry')
        self.db_entry.connect('changed',self.activate_save_button)
        self.banner_entry:Gtk.Entry = self.get_object('banner_entry')
        self.banner_entry.connect('changed',self.activate_save_button)
        self.coverart_entry:Gtk.Entry = self.get_object('coverart_entry')
        self.coverart_entry.connect('changed',self.activate_save_button)
        self.icon_entry:Gtk.Entry = self.get_object('icon_entry')
        self.icon_entry.connect('changed',self.activate_save_button)
        
        self.db_button:Gtk.Button = self.get_object('db_button')
        self.db_button.connect('clicked',self.select_folder)
        self.banner_button:Gtk.Button = self.get_object('banner_button')
        self.banner_button.connect('clicked',self.select_folder)
        self.coverart_button:Gtk.Button = self.get_object('coverart_button')
        self.coverart_button.connect('clicked',self.select_folder)
        self.icon_button:Gtk.Button = self.get_object('icon_button')
        self.icon_button.connect('clicked',self.select_folder)
        
        self.accept_button:Gtk.Button = self.get_object('accept_button')
        self.accept_button.connect('clicked',self.on_accept_button_clicked)
        self.cancel_button:Gtk.Button = self.get_object('cancel_button')
        self.cancel_button.connect('clicked',self.on_cancel_button_clicked)
        self.save_button:Gtk.Button = self.get_object('save_button')
        self.save_button.connect('clicked',self.on_save_button_clicked)
        
        self.setup_window()
        self.save_button.set_sensitive(False)
    def setup_window(self):
        self.api_entry.set_text(str(ConfigController.get_config('API','api_key')))
        self.db_entry.set_text(str(ConfigController.get_config('PATHS','db')))
        self.banner_entry.set_text(str(ConfigController.get_config('PATHS','banner')))
        self.coverart_entry.set_text(str(ConfigController.get_config('PATHS','coverart')))
        self.icon_entry.set_text(str(ConfigController.get_config('PATHS','icon')))
    
    def save_config(self):
        ConfigController.set_config('API','api_key',self.api_entry.get_text())
        ConfigController.set_config('PATHS','db',self.db_entry.get_text())
        ConfigController.set_config('PATHS','banner',self.banner_entry.get_text())
        ConfigController.set_config('PATHS','coverart',self.coverart_entry.get_text())
        ConfigController.set_config('PATHS','icon',self.icon_entry.get_text())
        ConfigController.save_config()
    
    def activate_save_button(self,widget):
        self.save_button.set_sensitive(True)
    
    def on_save_button_clicked(self,widget):
        self.save_config()
        self.save_button.set_sensitive(False)
    def on_cancel_button_clicked(self,widget):
        self.window.destroy()
    def on_accept_button_clicked(self,widget):
        self.save_config()
        self.window.destroy()
    def select_folder(self,widget):
        entry :Gtk.Entry
        dialog = SelectFolderDialog(self.window)
        match widget:
            case self.db_button:
                db_filter = Gtk.FileFilter()
                db_filter.set_name('Database')
                db_filter.add_mime_type('application/vnd.sqlite3')
                dialog = SelectFileDialog(self.window)
                dialog.create_filter(db_filter)
                entry = self.db_entry
            case self.banner_button:
                entry = self.banner_entry
            case self.coverart_button:
                entry = self.coverart_entry
            case self.icon_button:
                entry = self.icon_entry
        
        
        response = dialog.run()
        
        if response == Gtk.ResponseType.OK:
            entry.set_text(dialog.get_filename())
            
        dialog.destroy()