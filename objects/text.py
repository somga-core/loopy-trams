import pygame as pg
from settings import *

class Text:
    def __init__(self, text, color, position, size):
        self.text = text
        self.color = color
        self.position = position
        self.size = size

        self.update_image()

    def tick(self, window):
        pass

    def draw(self, window):
        image_surface_size = self.image_surface.get_size()
        image_surface_position = (
            self.position[0] - image_surface_size[0] // 2,
            self.position[1] - image_surface_size[1] // 2
        )
        window.drawing_surface.blit(self.image_surface, image_surface_position)

    def update_image(self):
        self.image_surface = FONT.render(self.text, True, self.color)
        self.image_surface = pg.transform.rotozoom(self.image_surface, 0, self.size)

    def change_text(self, text):
        self.text = text
        self.update_image()

    def change_color(self, color):
        self.color = color
        self.update_image()

    def change_size(self, size):
        self.size = size
        self.update_image()

    def change_position(self, position):
        self.position = position



