from scenes.scene import *

from objects.map import Map

class Game(Scene):
    def __init__(self, map_file):
        super().__init__()
        self.objects = [
            Map(map_file)
        ]