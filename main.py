from os.path import isfile
from time import time

from settings import *

import scenes
import scenes.menu

class Window:
    def __init__(self):
        self.setup()

    def mainloop(self):
        while self.run:
            delta_time = time() - self.last_update_time
            self.last_update_time += delta_time
            self.time_accumulator += delta_time
            
            while self.time_accumulator > SECONDS_PER_TICK:
                self.current_scene.tick(self)
                self.time_accumulator -= SECONDS_PER_TICK
                
            self.current_scene.draw(self)

    def setup(self):
        if not isfile("assets/mouse_dog.png"):
            quit()

        self.current_scene = scenes.menu.Menu()
        self.last_update_time = time()
        self.time_accumulator = 0
        self.run = True

    def change_current_scene(self, scene):
        self.current_scene = scene

if __name__ == "__main__":
    window = Window()
    window.mainloop()