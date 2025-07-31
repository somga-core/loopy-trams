from os.path import isfile
from time import time
import pygame as pg

from settings import *

import scenes.game
import scenes.levels
import scenes.menu
import scenes.scene

import objects.button
import objects.display
import objects.map
import objects.text

class Window:
    def __init__(self):
        if not isfile("assets/mouse_dog.png"):
            quit()

        pg.init()

        self.screen = pg.display.set_mode(STANDART_WINDOW_SCALE)
        self.font = pg.font.SysFont(None, 48)
        
        self.current_scene = scenes.menu.Menu(self)
        self.last_update_time = time()
        self.time_accumulator = 0
        self.run = True


    def mainloop(self):
        while self.run:
            self.time_accumulator += time() - self.last_update_time
            self.last_update_time = time()
            
            while self.time_accumulator > SECONDS_PER_TICK:
                self.current_scene.tick(self)
                self.time_accumulator -= SECONDS_PER_TICK
                
                for event in pg.event.get():
                    if event.type == pg.QUIT: self.run = False

            self.screen.fill((0, 0, 0))
            self.current_scene.draw(self)
            pg.display.update()

        pg.quit()

    def change_current_scene(self, scene):
        self.current_scene = scene

if __name__ == "__main__":
    window = Window()
    window.mainloop()
    quit()
