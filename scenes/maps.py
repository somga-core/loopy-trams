from scenes.scene import Scene
from scenes.game import Game

from objects.button import Button

class Maps(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.objects += [
            Button("assets/tram/tram_down_left.png", "assets/tram/tram_down_right.png", (0, 0), lambda: self.window.change_current_scene(Game(self.window, "tutorial"))),
        ]