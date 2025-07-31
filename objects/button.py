from objects.display import *

class Button(Display):
    def __init__(self):
        super().__init__()

    def tick(self, window):
        pass
    
    def draw(self, window):
        return super().draw(window)