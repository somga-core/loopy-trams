import pygame as pg

from objects.display import *

class Button(Display):
    def __init__(self, path_to_image, path_to_active_image, position, on_click_function):
        super().__init__(path_to_image, position)
        self.on_click_function = on_click_function
        self.active = False
        self.path_to_active_image = path_to_active_image
        self.path_to_image = path_to_image
        self.collide_with_cursor = False

    def tick(self, window):
        for event in window.event_handler:
            if event.type in (pg.MOUSEMOTION, pg.MOUSEBUTTONDOWN):
                self.check_collision(event.pos, window)

            if event.type == pg.MOUSEMOTION:
                if not self.active and self.collide_with_cursor:
                    self.active = True
                    self.update_image()
                elif self.active and not self.collide_with_cursor:
                    self.active = False
                    self.update_image()

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.collide_with_cursor:
                    self.on_click_function()

    def check_collision(self, mouse_position, window):
        image_surface_size = (self.image_surface.get_size()[0] * window.scale, self.image_surface.get_size()[1] * window.scale)
        image_surface_position = (window.drawing_surface_position[0] + self.position[0] * window.scale, window.drawing_surface_position[1] + self.position[1] * window.scale)
        self.collide_with_cursor = pg.rect.Rect(*image_surface_position, *image_surface_size).collidepoint(mouse_position)
    
    def change_image(self, path_to_image):
        self.path_to_image = path_to_image
        self.update_image()

    def change_active_image(self, path_to_active_image):
        self.path_to_active_image = path_to_active_image
        self.update_image()

    def update_image(self):
        if self.active:
            self.image_surface = pg.image.load(self.path_to_active_image)
        else:
            self.image_surface = pg.image.load(self.path_to_image)

    def draw(self, window):
        return super().draw(window)
