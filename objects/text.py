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
        window.drawing_surface.blit(self.image, self.position)

    def update_image(self):
        self.image = FONT.render(self.text, True, self.color)
        self.image = pg.transform.rotozoom(self.image, 0, self.size)

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



