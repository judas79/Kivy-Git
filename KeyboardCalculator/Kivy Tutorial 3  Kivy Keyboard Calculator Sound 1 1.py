# ---------- main.py  ----------

# all the functions reside here

import kivy

kivy.require("1.11.0")

# using both the Grid layout as well as the Box layout
# importing only the Grid library

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

# add sounds
from kivy.clock import Clock
from kivy.core.audio import SoundLoader


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
# Function called when equals is pressed

class KeyboardCalculator1App(App):

    def build(self):
        self.load_sounds()
        return CalcGridLayout()

    def load_sounds(self):
        self.sounds = {}
        for i in range(15):
            fname = 'sound' + str(i + 1) + '.wav'
            print(fname, '/n')
            self.sounds[i] = SoundLoader.load('\\Users\\Gina\\PycharmProjects\\Kivy\\sounds\\' + fname)



    def play_sound0(self):
        sound = self.sounds.get(0)
        if sound is not None:
            if sound.state == "play":
                sound.stop()

            sound.volume = 0.5
            sound.play()
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)

    def play_sound1(self):
        sound = self.sounds.get(1)
        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            sound.play()
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)

    def play_sound2(self):
        sound = self.sounds.get(2)
        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            sound.play()
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)

    def play_sound3(self):
        sound = self.sounds.get(3)
        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            sound.play()
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)

    def play_sound4(self):
        sound = self.sounds.get(4)
        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            sound.play()
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)

    def play_sound5(self):
        sound = self.sounds.get(5)
        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            sound.play()
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)

    def play_sound6(self):
        sound = self.sounds.get(6)
        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            sound.play()
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)



    def play_sound7(self):
        sound = self.sounds.get(7)
        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            sound.play()
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)

    def play_sound8(self):
        sound = self.sounds.get(8)
        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            sound.play()
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)

    def play_sound9(self, octave=None):
        sound = self.sounds.get(9)

        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            #sound.pitch = 2
            sound.play()

            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
           # print('text = ', str(octave))

    # addition sign
    def play_sound10(self, octave=None):
        sound = self.sounds.get(10)

        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            #sound.pitch = 2
            sound.play()

            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            #print('text = ', str(octave))

    # subtraction sign
    def play_sound11(self, octave=None):
        sound = self.sounds.get(11)

        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            #sound.pitch = 2
            sound.play()

            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            #print('text = ', str(octave))

    # multiplication sign
    def play_sound12(self, octave=None):
        sound = self.sounds.get(12)

        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            #sound.pitch = 2
            sound.play()

            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            #print('text = ', str(octave))

    # division sign
    def play_sound13(self, octave=None):
        sound = self.sounds.get(13)

        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            #sound.pitch = 2
            sound.play()

            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            #print('text = ', str(octave))

    # equals sign
    def play_sound14(self, octave=None):
        sound = self.sounds.get(14)

        if sound is not None:
            if sound.state == "play":
                sound.stop()
            sound.volume = 0.5
            #sound.pitch = 2
            sound.play()

            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            #print('text = ', str(octave))


calcApp = KeyboardCalculator1App()

calcApp.run()