import pygame as pg

class Display:
    def __init__(self, path_to_image, scale, position):
        self.image = pg.image.load(path_to_image)
        self.image.convert()
        self.image = pg.transform.rotozoom(self.image, 0, scale)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def tick(self, window):
        pass

    def draw(self, window):
        window.screen.blit(self.image, self.rect)

    def change_image(self, path_to_image, scale):
        self.image = pg.image.load(path_to_image)
        self.image.convert()
        self.image = pg.transform.rotozoom(self.image, 0, scale)
