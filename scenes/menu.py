from scenes.scene import *

from objects.button import Button
from objects.display import Display
from objects.text import Text

class Menu(Scene):
    def __init__(self, window):
        super().__init__(window)

        for object_to_append in [
            Display("assets/mouse_dog.png", 0.5, (0, 100)),
            Text("smaco", self.window.font, (255, 255, 255), (0, 0), 1)
        ]: self.objects.append(object_to_append)
