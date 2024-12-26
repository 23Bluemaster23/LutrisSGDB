import gi
import sys
gi.require_version("Gtk", "3.0")
from utils.CONSTANTS import STYLES_PATH
from gi.repository import Gtk,Gdk
from views.MainWindow import MainWindow
def on_activate(app):
    mw = MainWindow()
    mw.main_window.set_application(app)
    style_provider = Gtk.CssProvider()
    style_provider.load_from_path(STYLES_PATH)
    Gtk.StyleContext.add_provider_for_screen(
        screen=Gdk.Screen.get_default(),
        provider=style_provider,
        priority=Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    mw.main_window.present()
    mw.main_window.show_all()

if __name__ == '__main__':
    app = Gtk.Application()
    app.connect('activate',on_activate)
    app.run(sys.argv)
    
    