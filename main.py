from os.path import isfile
from time import time
import pygame as pg

pg.init()

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
            raise ImportError("mouse_dog.png is not found")

        self.screen = pg.display.set_mode(DEFAULT_WINDOW_SIZE, pg.RESIZABLE)
        self.drawing_surface = pg.Surface(INITIAL_GAME_SIZE)
        
        self.current_scene = scenes.menu.Menu()
        
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

            self.screen.fill((0, 0, 0))
            self.current_scene.draw(self)

            screen_size = pg.display.get_surface().get_size()
            scale = min(screen_size[0] / INITIAL_GAME_SIZE[0], screen_size[1] / INITIAL_GAME_SIZE[1])
 
            drawing_surface_size = (INITIAL_GAME_SIZE[0] * scale, INITIAL_GAME_SIZE[1] * scale)
            drawing_surface_position = (screen_size[0] // 2 - drawing_surface_size[0] // 2, screen_size[1] // 2 - drawing_surface_size[1] // 2)
            self.screen.blit(pg.transform.scale(self.drawing_surface, drawing_surface_size), drawing_surface_position)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
            pg.display.update()

        pg.quit()
        quit()

    def change_current_scene(self, scene):
        self.current_scene = scene

if __name__ == "__main__":
    window = Window()
    window.mainloop()
    quit()
