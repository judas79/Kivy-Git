Originally named sounds, the main python file has been renamed to KeyboardCalculator.  The path to open the .wave files, will have to be changed, to point to the directory the sound files are in: 
def load_sounds(self):
        self.sounds = {}
        for i in range(15):
            fname = 'sound' + str(i + 1) + '.wav'
            print(fname, '/n')
            self.sounds[i] = SoundLoader.load('\\Users\\Gina\\PycharmProjects\\Kivy\\sounds\\' + fname)

change this line, for Windows:

self.sounds[i] = SoundLoader.load('\\ *Path to the sounds directory* \\' + fname)

The octave setting would not work on my machine, fix it if you can.  sound.pitch = 2  are all commented out.  My dependencies where installed....
