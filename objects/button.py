import pygame as pg

from objects.display import *

class Button(Display):
    def __init__(self, path_to_image, position, event):
        super().__init__(path_to_image, position)
        self.event = event

    def tick(self, window):
        for event in window.event_handler:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.image_surface.get_rect(topleft=self.position).collidepoint(event.pos):
                    window.event_queue.append(self.event)
    
    def draw(self, window):
        return super().draw(window)
