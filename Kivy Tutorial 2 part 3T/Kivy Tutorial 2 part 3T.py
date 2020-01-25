# ---------- KIVYTUT3.PY ----------

import kivy

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


# A Float layout positions and sizes objects as a percentage
# of the window size

class GridLayoutApp(App):

    def build(self):
        return GridLayout()


gridApp = GridLayoutApp()

gridApp.run()