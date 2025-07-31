import time

class Scene:
    def __init__(self):
        self.objects = []

    def draw(self, window):
        for object in self.objects:
            object.draw(window)

    def tick(self, window):
        print(time.time())
        for object in self.objects:
            object.tick(window)