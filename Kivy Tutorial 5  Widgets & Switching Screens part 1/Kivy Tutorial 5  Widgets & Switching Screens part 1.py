# ---------- KIVY TUTORIAL PT 5  ----------

# Checkbox,Radio Buttons, Switch,Popups,
# Spinners, Tabbed Panels & Switching Screens

# ---------- kivytut.py  ----------

import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup

# Used to create and display popup
class CustomPopup(Popup):
    pass

# create main class layout
class SampleBoxLayout(BoxLayout):

    # for checkbox, create object properties, to comunicate between,
    # this main pa file and the .kv file
    checkbox_is_active = ObjectProperty(False)

    # create function that the checkbox will be calling.
    # Value from, the checkbox selections

    def checkbox_18_clicked(self, instance, value):

        # if the value from the checkbox is true
        if value is True:
            print('Checkbox Checked')

        else:
            print('Checkbox is Unchecked')

# *********** radio buttons which are actually grouped checkboxes *********

    # create 3 objects properties, for the user to pick a color from
    # one button only, can be True at a time, with radio buttons, the other two set to False
    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

# ************ handle a Switch ******************

    def switch_on(self, instance, value):

        # if the value from the switch is true
        if value is True:
            print('Switch on')

        else:
            print('Switch off')

# ************ handles opening a popup ********************

    # this will open up every time it is called
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

# ************** handles our spinner **********************

    # grab different values from the spinner widget and
    # dependant on what is picked print to the console
    def spinner_clicked(self, value):
        print('spinner value: ' + value)

# ********* Create sample app and its App methods *********

class SampleApp(App):

    # build the interface
    def build(self):

        # change the background color in the app window
        Window.clearcolor = (1, 1, 1, 1)
        return SampleBoxLayout()

sample_app = SampleApp()

sample_app.run()