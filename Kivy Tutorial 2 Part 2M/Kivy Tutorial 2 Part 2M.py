# It is common practice to create your own custom
# widgets so base widgets aren't effected

# examples of 5 Kivy Layouts, Custom Widgets,
# and default attributes

import kivy
kivy.require('1.11.1')

# to be able to use all the fields and methods of kivy

from kivy.app import App

# to make a *** FLOATING LAYOUT ***
# to position buttons

from kivy.uix.floatlayout import FloatLayout


# create the class that will tie in with the App kv file

class FloatingMINEApp(App):

    # call for this widget to be built

    def build(self):

        return FloatLayout()

floatingMINE = FloatingMINEApp()

floatingMINE.run()