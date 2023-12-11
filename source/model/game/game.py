import subprocess

class Game:
    '''running the game executable'''

    def __init__(self, dir_exe):
        self.exec = dir_exe

    def run(self):
        subprocess.run([self.exec])

