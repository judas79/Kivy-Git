# It is common practice to create your own custom
# widgets so base widgets aren't effected

# examples of 5 Kivy Layouts, Custom Widgets,
# and default attributes

import kivy
kivy.require('1.11.1')

# to be able to use all the fields and methods of kivy

from kivy.app import App

# ot make a custom widget
from kivy.uix.widget import Widget

# pass in Widget
class CustomWidget(Widget):

    # pass used as a place holder for this class

    pass

# create the class that will tie in with the App kv file

class CustomWidgetApp(App):

    # call for this widget to be built

    def build(self):

        return CustomWidget()

customWidget = CustomWidgetApp()

customWidget.run()