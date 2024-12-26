import gi
import threading
from gi.repository import Gtk

class CompletedDialog(Gtk.Builder):
    def __init__(self):
        super().__init__()
        self.add_from_file('templates/CompletedDialog.glade')
        self.dialog:Gtk.Dialog = self.get_object('CompletedDialog') 