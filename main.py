import gi
import time



gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os
os.system("clear")
clicks = 0

class ButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="CLICK COUNTER")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Click Me")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_hi")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_bye")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):

        global clicks
        os.system("clear")
        clicks = clicks + 1
        print(clicks)

    def on_open_clicked(self, button):
        print("hi")
        
        
    def on_close_clicked(self, button):
        print("bye")
        time.sleep(0.1)
        win.destroy()
        





win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
