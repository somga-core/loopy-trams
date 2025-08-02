from settings import *

from scenes.scene import Scene
import scenes.game

import json

from objects.button import Button
from objects.display import Display
from objects.text import Text

class Maps(Scene):
    def __init__(self, window):
        super().__init__(window)
        with open("save.json") as f:
            save = json.load(f)
        
        self.current_map_page = 0

        if save:
            self.current_map_page = MAP_ORDER.index([i for i in save][-1])
        
        self.objects += [
            Display("assets/backgrounds/blackout.png",
                    (0, 0)),

            Text("",
                 (255, 255, 255),
                 (320, 240),
                 1),

            Text("",
                 (255, 255, 255),
                 (320, 280),
                 .5),

            Text("",
                 (255, 255, 255),
                 (320, 295),
                 .5),

            Text("",
                 (255, 255, 255),
                 (320, 310),
                 .5),

            Button("assets/buttons/unactive/button_enter_unactive.png",
                   "assets/buttons/active/button_enter_active.png",
                   (320 + 32, 320),
                   lambda: self.window.change_current_scene(scenes.game.Game(self.window, MAP_ORDER[self.current_map_page%len(MAP_ORDER)]))),
        
            Button("assets/buttons/unactive/button_left_unactive.png",
                   "assets/buttons/active/button_left_active.png",
                   (320 - 130 - 32, 240 - 32),
                   lambda: self.change_map_page(-1)),
                   
            Button("assets/buttons/unactive/button_right_unactive.png",
                   "assets/buttons/active/button_right_active.png",
                   (320 + 130 - 32, 240 - 32),
                   lambda: self.change_map_page(1)),

            Button("assets/buttons/unactive/button_leave_unactive.png",
                   "assets/buttons/active/button_leave_active.png",
                   (320 - 96, 320),
                   self.leave)
        ]
        self.change_map_page(0)

    def leave(self):
        self.window.run = False

    def show_map_time(self):
        map_name = MAP_ORDER[self.current_map_page%len(MAP_ORDER)]

        with open("save.json") as f:
            save = json.load(f)

        if not map_name in save:
            save[map_name] = 0

        with open("maps/" + map_name + ".json") as f:
            map_data = json.load(f)

        self.objects[2].change_text(f"Best time: {str(int(save[map_name]) // 60).rjust(2, '0')}:{str(int(save[map_name]) % 60).rjust(2, '0')}")
        self.objects[3].change_text(f"Complete time: {str(int(map_data['complete_time']) // 60).rjust(2, '0')}:{str(int(map_data['complete_time']) % 60).rjust(2, '0')}")
        self.objects[4].change_text(f"{'Completed!' if save[map_name] >= map_data['complete_time'] else 'Incomplete'}")

    def change_map_page(self, shift):
        self.current_map_page += shift
        self.objects[1].change_text(MAP_ORDER[self.current_map_page%len(MAP_ORDER)].title().replace("_", " "))
        self.show_map_time()