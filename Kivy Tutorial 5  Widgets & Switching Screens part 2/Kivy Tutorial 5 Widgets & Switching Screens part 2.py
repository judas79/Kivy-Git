import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# ***************** Switch Screens ******************

# You can create all your code including your kv code in the Python file
# using Builder.load_string(''' "everything goes within the triple quoutes ''')
Builder.load_string('''

# there will be two screens
<ScreenOne>:

    # everything follows the same protocols as shown in the prior examples;
    # that had a separate .kv file
    BoxLayout:
    
        # press a button to open screen 2
        Button:
            text:'Go to screen 2'
            on_press:
            
                # define the direction the screen is going to slide in and 
                # duration, it will take to do so
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                
                root.manager.current = 'screen_two'
                
<ScreenTwo>:

    # everything follows the same protocols as shown in the prior examples;
    # that had a separate .kv file
    BoxLayout:
    
        # press a button to open screen 1
        Button:
            text:'Go to screen 1'
            on_press:
            
                # define the direction the screen is going to slide in and 
                # duration, it will take to do so
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                
                root.manager.current = 'screen_one'
''')

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

# call the screen manager to be able to switch between screens
screen_manager = ScreenManager()

# apply the screen names as defined above 'screen_one', 'screen_two', to the screen_manager
screen_manager.add_widget(ScreenOne(name='screen_one'))
screen_manager.add_widget(ScreenTwo(name='screen_two'))

# make a class so out apps will run

class KivyTutorial5Part2App(App):

    def build(self):
        return screen_manager

kt5p2 = KivyTutorial5Part2App()

kt5p2.run()
