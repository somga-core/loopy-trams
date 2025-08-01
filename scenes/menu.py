from scenes.scene import Scene
from scenes.maps import Maps

from objects.button import Button
from objects.display import Display
from objects.text import Text

class Menu(Scene):
    def __init__(self, window):
        super().__init__(window)

        self.objects += [
            Button("assets/tram/tram_down_left.png", "assets/tram/tram_down_right.png", (0, 0), lambda: self.window.change_current_scene(Maps(self.window))),
            Display("assets/tiles/asphalt.png", (0, 100)),
            Text("Press LMB to continue", (255, 255, 255), (320, 340), .5)
        ]
