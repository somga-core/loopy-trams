from scenes.scene import *

from objects.button import Button
from objects.display import Display
from objects.text import Text

class Menu(Scene):
    def __init__(self):
        super().__init__()

        self.objects += [
            Display("assets/tiles/asphalt.png", (0, 100)),
            Text("smaco", (255, 255, 255), (0, 0), 1),
            Button("assets/tram/tram_down_left.png", "assets/tram/tram_down_right.png", (200, 0), lambda: print("hi"))
        ]
