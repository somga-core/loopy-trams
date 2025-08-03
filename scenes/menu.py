from scenes.scene import Scene
from scenes.maps import Maps

from objects.button import Button
from objects.display import Display
from objects.text import Text

class Menu(Scene):
    def __init__(self, window):
        super().__init__(window)

        self.objects += [
            Button(
                "assets/backgrounds/blackout.png",
                "assets/backgrounds/blackout.png",
                (0, 0),
                lambda: self.window.change_current_scene(Maps(self.window)),
                "assets/sounds/button_click.wav"
            ),
            Display(
                "assets/backgrounds/logo.png",
                (320 - 128, 240 - 99)
            ),
            Text("Click there to continue", (255, 255, 255), (320, 340), .5)
        ]
