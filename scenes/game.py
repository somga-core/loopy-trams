import json

from settings import *

from objects.button import Button
from objects.display import Display

class Game():
    def __init__(self, map_file):
        with open(map_file) as f:
            map_data = json.load(f)

        self.map = map_data["map"]
        self.damaged_tiles_appering_precent = map_data["damaged_tiles_appering_precent"]

        self.tiles = []
        self.trams = []

        for y in range(len(self.map)):
            self.tiles.append([])
            for x in range(len(self.map[y])):
                self.tiles[y].append(0)
                self.change_tile_type(x, y, self.map[y][x])

    def change_tile_type(self, x, y, type):
        if type in SPECIAL_TILES_LOOKUP:
            tile_data = SPECIAL_TILES_LOOKUP[type]
            self.tiles[y][x] = Button(tile_data[0], tile_data[0], (x * TILE_SIZE, y * TILE_SIZE), lambda: self.change_tile_type(x, y, tile_data[1]))
        else: 
            self.tiles[y][x] = Display(TILES_LOOKUP[type], (x * TILE_SIZE, y * TILE_SIZE))
        self.tiles[y][x].type = type

    def get_tile_type(self, x, y):
        return self.tiles[y][x].type

    def tick(self, window):
        for tile_row in self.tiles:
            for tile in tile_row:
                tile.tick(window)

        for tram in self.trams:
            pass

    def draw(self, window):
        for tile_row in self.tiles:
            for tile in tile_row:
                tile.draw(window)

        for tram in self.trams:
            tram.draw(window)