# ---------- KIVY TUTORIAL PT 4  ----------

# In this part of my Kivy tutorial I'll show how to use
# the ListView, ListAdapter and how to create a toolbar

# ---------- studentdb.py  ----------

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView




class StudentListButton(RecycleView):
    def __init__(self, **kwargs):
        super(StudentListButton, self).__init__(**kwargs)

        self.data = [{'text': str(x)} for x in range(20)]

# main class
class StudentDB(BoxLayout):

    # Connects the value in the TextInput widget
    # to these fields
    # what object properties will be needed?

    # a first name text input object
    # to put in or change first name information
    # and last name and student list

    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    # to submit students information

    def submit_student(self):

        # Get the student name from the TextInputs

        student_name = self.first_name_text_input.text + ' ' + self.last_name_text_input.text


    # to take students information off

    def delete_student(self):
        pass

    # to replace students information

    def replace_sudent(self):
        pass

# create the actual app portion; passing App in

class StudentDBApp(App):
    def build(self):
        return StudentDB()


dbApp = StudentDBApp()

dbApp.run()
