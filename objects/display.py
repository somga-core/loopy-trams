import pygame as pg
from settings import *

class Display:
    def __init__(self, path_to_image, position):
        self.position = position
        self.image_surface = pg.image.load(path_to_image)

    def tick(self, window):
        pass

    def draw(self, window):
        window.drawing_surface.blit(self.image_surface, self.position)

    def change_image(self, path_to_image):
        self.image_surface = pg.image.load(path_to_image)

    def change_position(self, position):
        self.position = position
