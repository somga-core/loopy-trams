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

        self.tiles = []
        
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
                   lambda: self.window.change_current_scene(scenes.game.Game(self.window, MAP_ORDER[self.current_map_page%len(MAP_ORDER)])),
                   "assets/sounds/button_click.wav"),
        
            Button("assets/buttons/unactive/button_left_unactive.png",
                   "assets/buttons/active/button_left_active.png",
                   (320 - 230 - 32, 240 - 32),
                   lambda: self.change_map_page(-1),
                   "assets/sounds/button_click.wav"),
                   
            Button("assets/buttons/unactive/button_right_unactive.png",
                   "assets/buttons/active/button_right_active.png",
                   (320 + 230 - 32, 240 - 32),
                   lambda: self.change_map_page(1),
                   "assets/sounds/button_click.wav"),

            Button("assets/buttons/unactive/button_leave_unactive.png",
                   "assets/buttons/active/button_leave_active.png",
                   (320 - 96, 320),
                   self.leave,
                   "assets/sounds/button_click.wav")
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
            self.map_data = json.load(f)

        self.objects[2].change_text(f"Best time: {str(int(save[map_name]) // 60).rjust(2, '0')}:{str(int(save[map_name]) % 60).rjust(2, '0')}")
        self.objects[3].change_text(f"Complete time: {str(int(self.map_data['complete_time']) // 60).rjust(2, '0')}:{str(int(self.map_data['complete_time']) % 60).rjust(2, '0')}")
        self.objects[4].change_text(f"{'Completed!' if save[map_name] >= self.map_data['complete_time'] else 'Incomplete'}")

    def load_map(self):
        raw_tiles = self.map_data["tiles"]

        self.tiles.clear()

        for y in range(len(raw_tiles)):
            for x in range(len(raw_tiles[y])):
                tile_type = raw_tiles[y][x]
                tile_image = TILES_LOOKUP[tile_type] if tile_type in TILES_LOOKUP else SPECIAL_TILES_LOOKUP[tile_type][0]
                self.tiles.append(Display(tile_image, (x * TILE_SIZE, y * TILE_SIZE)))

    def change_map_page(self, shift):
        self.current_map_page += shift
        self.objects[1].change_text(MAP_ORDER[self.current_map_page%len(MAP_ORDER)].title().replace("_", " "))
        self.show_map_time()
        self.load_map()

    def draw(self):
        for tile in self.tiles:
            tile.draw(self.window)
        super().draw()