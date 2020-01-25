# ---------- main.py  ----------

# all the functions reside here

import kivy

kivy.require("1.9.0")

# using both the Grid layout as well as the Box layout
# importing only the Grid library

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

# custom class, Passing in GridLayout
class CalcGridLayout(GridLayout):

    # when the equal sign is clicked get the text (number) and pass it in
    # and do the calculation

    def calculate(self, calculation):

        if calculation:

            # error protection

            try:

                # get the text out of the text entry area in the kv file
                # turn it int a string

                self.display.text = str(eval(calculation))

            # if an error occured

            except Exception:

                self.display.text = 'error'
                
# Function called when equals is pressed, Then the function calls the calculator.kv file

class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

calcApp = CalculatorApp()

calcApp.run()
