import pygame as pg

class Scene:
    def __init__(self, window):
        self.window = window
        self.objects = []

    def draw(self):
        for object_to_draw in self.objects:
            object_to_draw.draw(self.window)

    def tick(self):
        for object_to_tick in self.objects:
            object_to_tick.tick(self.window)
