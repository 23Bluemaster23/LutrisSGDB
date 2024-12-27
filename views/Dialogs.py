import gi
import threading
from gi.repository import Gtk

class CompletedDialog(Gtk.Builder):
    def __init__(self):
        super().__init__()
        self.add_from_file('templates/CompletedDialog.glade')
        self.dialog:Gtk.Dialog = self.get_object('CompletedDialog') 
        
class SelectFileDialog(Gtk.FileChooserDialog):
    def __init__(self,parent):
        super().__init__(
            title='Select Folder',
            parent=parent,
            action=Gtk.FileChooserAction.OPEN,
            )
        
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,"Select",Gtk.ResponseType.OK
        )
    
    def create_filter(self,filter:Gtk.FileFilter):
        self.add_filter(filter)
    
class SelectFolderDialog(Gtk.FileChooserDialog):
    def __init__(self,parent):
        super().__init__(
            title='Select Folder',
            parent=parent,
            action=Gtk.FileChooserAction.SELECT_FOLDER,
            )
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,"Select",Gtk.ResponseType.OK
        )