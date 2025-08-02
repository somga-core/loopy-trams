import json

from settings import *

from scenes.scene import Scene
import scenes.maps

from random import random, randint

from objects.button import Button
from objects.text import Text
from objects.display import Display

class Game(Scene):
    def __init__(self, window, map):
        super().__init__(window)

        with open("maps/" + map + ".json") as f:
            map_data = json.load(f)

        self.objects += [
            Button(
                "assets/buttons/unactive/button_leave_unactive.png",
                "assets/buttons/active/button_leave_active.png",
                (0, 0),
                self.leave
            ),
            Text("00:00", (255, 255, 255), (110, 32), .5),
            Text(map_data["text"], (255, 255, 255), (320, 440), .5)
        ]

        self.window = window
        self.timer = 0

        self.map_name = map

        self.raw_tiles = map_data["tiles"]
        self.raw_trams = map_data["trams"]
        self.tram_speed = map_data["tram_speed"]
        self.complete_time = map_data["complete_time"]
        self.tram_untouchable_radius = map_data["tram_untouchable_radius"]
        self.damaged_tiles_appearing_probability = map_data["damaged_tiles_appearing_probability"]

        self.game_state = 0
        self.tram_running = True

        self.tiles = []
        self.trams = []

        for y in range(len(self.raw_tiles)):
            self.tiles.append([])
            for x in range(len(self.raw_tiles[y])):
                self.tiles[y].append(0)
                self.change_tile_type(x, y, self.raw_tiles[y][x])

        for tram in self.raw_trams:
            self.trams.append(
                Display(
                    TRAM_LOOKUP[tram[2]][0],
                    (
                        TILE_SIZE * tram[0] - TILE_SIZE // 2,
                        TILE_SIZE * tram[1] - TILE_SIZE // 2
                    )
                )
            )
            self.trams[-1].direction = tram[2]

    def change_tile_type(self, x, y, type):
        if not self.get_tile_occupied(x, y) and self.tram_running:
            if type in SPECIAL_TILES_LOOKUP:
                tile_data = SPECIAL_TILES_LOOKUP[type]
                self.tiles[y][x] = Button(
                    tile_data[0],
                    tile_data[0],
                    (x * TILE_SIZE, y * TILE_SIZE),
                    lambda: self.change_tile_type(x, y, tile_data[1])
                )
            else: 
                self.tiles[y][x] = Display(TILES_LOOKUP[type], (x * TILE_SIZE, y * TILE_SIZE))
            self.tiles[y][x].type = type

    def get_tile_occupied(self, x, y):
        for tram in self.trams:
            if self.get_tile_position_under_tram(tram) == (x, y):
                return True
        return False

    def get_tile_type(self, x, y):
        return self.tiles[y][x].type

    def get_tile_position_under_tram(self, tram):
        tram_position = tram.get_position()
        return (tram_position[0] // TILE_SIZE + 1, tram_position[1] // TILE_SIZE + 1)
    
    def get_tile_position_in_front_of_tram(self, tram):
        tile_position_under_tram = self.get_tile_position_under_tram(tram)
        tile_type_under_tram = self.get_tile_type(*tile_position_under_tram)

        if tram.direction in ("u", "d", "r", "l"):
            tile_shift = TRAM_LOOKUP[tram.direction][1]
        else:
            if tram.direction == "dl":
                if tile_type_under_tram in (")", "q", "t"):
                    tile_shift = (-1, 0)
                elif tile_type_under_tram in ("[", "r", "i"):
                    tile_shift = (0, -1)
            elif tram.direction == "dr":
                if tile_type_under_tram in ("(", "w", "y"):
                    tile_shift = (1, 0)
                elif tile_type_under_tram in ("]", "e", "u"):
                    tile_shift = (0, -1)
            elif tram.direction == "ul":
                if tile_type_under_tram in ("]", "e", "u"):
                    tile_shift = (-1, 0)
                elif tile_type_under_tram in ("(", "w", "y"):
                    tile_shift = (0, 1)
            elif tram.direction == "ur":
                if tile_type_under_tram in ("[", "r", "i"):
                    tile_shift = (1, 0)
                elif tile_type_under_tram in (")", "q", "t"):
                    tile_shift = (0, 1)

        return (tile_position_under_tram[0] + tile_shift[0], tile_position_under_tram[1] + tile_shift[1])

    def update_tram_direction(self, tram):
        tile_position_under_tram = self.get_tile_position_under_tram(tram)
        tile_type_under_tram = self.get_tile_type(*tile_position_under_tram)
        last_tram_direction = tram.direction

        if tram.direction == "u":
            if tile_type_under_tram in (")", "q", "t"):
                tram.direction = "dl"
            elif tile_type_under_tram in ("(", "w", "y"):
                tram.direction = "dr"
        elif tram.direction == "d":
            if tile_type_under_tram in ("]", "e", "u"):
                tram.direction = "ul"
            elif tile_type_under_tram in ("[", "r", "i"):
                tram.direction = "ur"
        elif tram.direction == "r":
            if tile_type_under_tram in ("]", "e", "u"):
                tram.direction = "dr"
            elif tile_type_under_tram in (")", "q", "t"):
                tram.direction = "ur"
        elif tram.direction == "l":
            if tile_type_under_tram in ("[", "r", "i"):
                tram.direction = "dl"
            elif tile_type_under_tram in ("(", "w", "y"):
                tram.direction = "ul"
        elif tram.direction == "dl":
            if tile_type_under_tram in ("=", "+"):
                tram.direction = "l"
            elif tile_type_under_tram in ("|", "x"):
                tram.direction = "u"
        elif tram.direction == "dr":
            if tile_type_under_tram in ("=", "+"):
                tram.direction = "r"
            elif tile_type_under_tram in ("|", "x"):
                tram.direction = "u"
        elif tram.direction == "ul":
            if tile_type_under_tram in ("=", "+"):
                tram.direction = "l"
            elif tile_type_under_tram in ("|", "x"):
                tram.direction = "d"
        elif tram.direction == "ur":
            if tile_type_under_tram in ("=", "+"):
                tram.direction = "r"
            elif tile_type_under_tram in ("|", "x"):
                tram.direction = "d"

        if last_tram_direction != tram.direction:
            self.align_tram(tram)

    def explode_tram(self, tram):
        tram.change_image("assets/tram/explotion.png")
        self.game_state = -1
        self.leave()

    def leave(self):
        if self.tram_running == True:
            self.tram_running = False

            if self.game_state == 0:
                self.objects += [
                    Display("assets/backgrounds/blackout.png", (0, 0)),
                    Text("Are you sure you want to leave?", (255, 255, 255), (320, 200), .7),
                    Button(
                        "assets/buttons/unactive/button_leave_unactive.png",
                        "assets/buttons/active/button_leave_active.png",
                        (320-96, 250),
                        self.save_and_exit
                    ),
                    Button(
                        "assets/buttons/unactive/button_right_unactive.png",
                        "assets/buttons/active/button_right_active.png",
                        (320+32, 250),
                        self.cancel_leave
                    )
                ]

            if self.game_state == 1:
                self.objects += [
                    Display("assets/backgrounds/blackout.png", (0, 0)),
                    Button(
                        "assets/buttons/unactive/button_leave_unactive.png",
                        "assets/buttons/active/button_leave_active.png",
                        (320-96, 250),
                        self.save_and_exit
                    ),
                ]
                next_map_index = MAP_ORDER.index(self.map_name) + 1
                
                if len(MAP_ORDER) - 1 >= next_map_index:
                    next_map = MAP_ORDER[next_map_index]
                    self.objects += [
                        Text("You completed the map!", (255, 255, 255), (320, 200), .7),
                        Button(
                            "assets/buttons/unactive/button_right_unactive.png",
                            "assets/buttons/active/button_right_active.png",
                            (320+32, 250),
                            lambda: self.window.change_current_scene(Game(self.window, next_map))
                        )
                    ]
                else:
                    self.objects += [
                        Text("You completed the last map!", (255, 255, 255), (320, 200), .7),
                        Button(
                            "assets/buttons/unactive/button_replay_unactive.png",
                            "assets/buttons/active/button_replay_active.png",
                            (320+32, 250),
                            lambda: self.window.change_current_scene(Game(self.window, self.map_name))
                        )
                    ]

            if self.game_state == -1:
                self.objects += [
                    Display("assets/backgrounds/blackout.png", (0, 0)),
                    Text("One of the trams exploded!", (255, 255, 255), (320, 200), .7),
                    Button(
                        "assets/buttons/unactive/button_leave_unactive.png",
                        "assets/buttons/active/button_leave_active.png",
                        (320-96, 250),
                        self.save_and_exit
                    ),
                    Button(
                        "assets/buttons/unactive/button_replay_unactive.png",
                        "assets/buttons/active/button_replay_active.png",
                        (320+32, 250),
                        lambda: self.window.change_current_scene(Game(self.window, self.map_name))
                    )
                ]

    def cancel_leave(self):
        self.tram_running = True
        self.objects = self.objects[:3]

    def save_and_exit(self):
        with open("save.json") as f:
            save = json.load(f)

        if not (self.map_name in save and save[self.map_name] > self.timer):
            save[self.map_name] = self.timer

        with open("save.json", "w") as f:
            json.dump(save, f)

        self.window.change_current_scene(scenes.maps.Maps(self.window))

    def align_tram(self, tram):
        tram_position = list(tram.get_position())
        
        tram_position[0] = round(tram_position[0] / 16) * 16
        tram_position[1] = round(tram_position[1] / 16) * 16

        tram.change_position(tram_position)

        self.move_tram(tram)

    def update_tram_image(self, tram):
        tram.change_image(TRAM_LOOKUP[tram.direction][0])

    def get_collision(self, tram):
        tile_position_in_front_of_tram = self.get_tile_position_in_front_of_tram(tram)
        tile_type_in_front_of_tram = self.get_tile_type(*tile_position_in_front_of_tram)

        if tile_type_in_front_of_tram in ("h", "v", "."):
            return True
        elif self.get_tile_occupied(*tile_position_in_front_of_tram):
            return True
        elif tram.direction == "u":
            if tile_type_in_front_of_tram in ("+", "[", "]", "=", "e", "r", "u", "i", "a", "s", "d", "f"):
                return True
        elif tram.direction == "d":
            if tile_type_in_front_of_tram in ("+", "(", ")", "=", "q", "w", "t", "y", "a", "s", "d", "f"):
                return True
        elif tram.direction == "l":
            if tile_type_in_front_of_tram in ("x", ")", "]", "|", "q", "e", "t", "u", "g", "j", "k", "l"):
                return True
        elif tram.direction == "r":
            if tile_type_in_front_of_tram in ("x", "(", "[", "|", "w", "r", "y", "i", "g", "j", "k", "l"):
                return True
        
        return False
    
    def move_tram(self, tram):
        tram_position = tram.get_position()
        tram_acceleration = TRAM_LOOKUP[tram.direction][1]
        tram.change_position(
            (
                tram_position[0] + tram_acceleration[0] * self.tram_speed,
                tram_position[1] + tram_acceleration[1] * self.tram_speed
            )
        )

    def get_tram_around(self, x, y):
        for tram in self.trams:
            tram_position = self.get_tile_position_under_tram(tram)

            if abs(tram_position[0] - x) <= self.tram_untouchable_radius and abs(tram_position[1] - y) <= self.tram_untouchable_radius:
                return True
        
        return False

    def generate_damaged_rails(self):
        tile_y = randint(0, len(self.raw_tiles) - 1)
        tile_x = randint(0, len(self.raw_tiles[0]) - 1)

        tile_type = self.get_tile_type(tile_x, tile_y)

        if not self.get_tram_around(tile_x, tile_y):
            if tile_type == "=":
                self.change_tile_type(tile_x, tile_y, "h")
            elif tile_type == "|":
                self.change_tile_type(tile_x, tile_y, "v")

    def tick(self):
        if self.tram_running:
            self.timer += .05
            timer_text = ""
            timer_text += f"{str(int(self.timer) // 60).rjust(2, '0')}:{str(int(self.timer) % 60).rjust(2, '0')}"
            timer_text += " / "
            timer_text += f"{str(int(self.complete_time) // 60).rjust(2, '0')}:{str(int(self.complete_time) % 60).rjust(2, '0')}"
            self.objects[1].change_text(timer_text)

            if random() <= self.damaged_tiles_appearing_probability:
                self.generate_damaged_rails()

            for tile_row in self.tiles:
                for tile in tile_row:
                    tile.tick(self.window)

            for tram in self.trams:
                self.update_tram_direction(tram)
                self.update_tram_image(tram)
                if not self.get_collision(tram):
                    self.move_tram(tram)
                else:
                    self.explode_tram(tram)
            
            if self.timer >= self.complete_time:
                self.game_state = 1
                self.leave()

        super().tick()

    def draw(self):
        for tile_row in self.tiles:
            for tile in tile_row:
                tile.draw(self.window)

        for tram in self.trams:
            tram.draw(self.window)

        super().draw()