import pygame as pg

class Scene:
    def __init__(self):
        self.objects = []

    def draw(self, window):
        for object_to_draw in self.objects:
            object_to_draw.draw(window)

    def tick(self, window):
        for object_to_tick in self.objects:
            object_to_tick.tick(window)
