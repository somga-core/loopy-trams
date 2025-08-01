from settings import *

from scenes.scene import Scene
from scenes.game import Game

from objects.button import Button
from objects.display import Display
from objects.text import Text

class Maps(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.current_map_page = 0
        self.objects += [
            Display("assets/mouse_dog.png",
                    (0, 0)),

            Text(MAP_ORDER[self.current_map_page].title(),
                 (255, 255, 255),
                 (320, 240),
                 1),

            Button("assets/tram/tram_horisontal.png",
                   "assets/tram/tram_vertical.png",
                   (320 - 32, 480 - 64),
                   lambda: self.window.change_current_scene(Game(self.window, MAP_ORDER[self.current_map_page%len(MAP_ORDER)]))),
        
            Button("assets/tram/tram_horisontal.png",
                   "assets/tram/tram_vertical.png",
                   (0, 240 - 32),
                   lambda: self.change_map_page(-1)),
                   
            Button("assets/tram/tram_horisontal.png",
                   "assets/tram/tram_vertical.png",
                   (640 - 64, 240 - 32),
                   lambda: self.change_map_page(1))
        ]

    def change_map_page(self, shift):
        self.current_map_page += shift
        self.objects[1].change_text(MAP_ORDER[self.current_map_page%len(MAP_ORDER)].title().replace("_", " "))
