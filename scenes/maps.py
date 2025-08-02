from scenes.scene import Scene
import scenes.game

from objects.button import Button

class Maps(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.objects += [
            Button(
                "assets/tram/tram_down_left.png",
                "assets/tram/tram_down_right.png",
                (0, 0),
                lambda: self.window.change_current_scene(scenes.game.Game(self.window, "tutorial"))
            ),
        ]