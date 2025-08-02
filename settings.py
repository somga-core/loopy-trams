import pygame as pg

SECONDS_PER_TICK = .05
DEFAULT_WINDOW_SIZE = (640, 480)
INITIAL_GAME_SIZE = (640, 480)
FONT = pg.font.Font("assets/font/Oldtimer.ttf", 25)
TILE_SIZE = 32

TILES_LOOKUP = {
    ".": "assets/tiles/asphalt.png",

    "=": "assets/tiles/rails/one_way/rails_horisontal.png",
    "|": "assets/tiles/rails/one_way/rails_vertical.png",

    ")": "assets/tiles/rails/one_way/rails_down_left.png",
    "(": "assets/tiles/rails/one_way/rails_down_right.png",
    "]": "assets/tiles/rails/one_way/rails_up_left.png",
    "[": "assets/tiles/rails/one_way/rails_up_right.png",
    "=": "assets/tiles/rails/one_way/rails_horisontal.png",
    "|": "assets/tiles/rails/one_way/rails_vertical.png"
}

SPECIAL_TILES_LOOKUP = {
    "h": ("assets/tiles/rails/one_way/rails_horisontal_damaged.png", "="),
    "v": ("assets/tiles/rails/one_way/rails_vertical_damaged.png", "|"),

    "+": ("assets/tiles/rails/two_ways/rails_cross_horisontal.png", "x"),
    "x": ("assets/tiles/rails/two_ways/rails_cross_vertical.png", "+"),

    "q": ("assets/tiles/rails/two_ways/turn/rails_down_left_horisontal.png", "a"),
    "w": ("assets/tiles/rails/two_ways/turn/rails_down_right_horisontal.png", "s"),
    "e": ("assets/tiles/rails/two_ways/turn/rails_up_left_horisontal.png", "d"),
    "r": ("assets/tiles/rails/two_ways/turn/rails_up_right_horisontal.png", "f"),

    "t": ("assets/tiles/rails/two_ways/turn/rails_down_left_vertical.png", "g"),
    "y": ("assets/tiles/rails/two_ways/turn/rails_down_right_vertical.png", "j"),
    "u": ("assets/tiles/rails/two_ways/turn/rails_up_left_vertical.png", "k"),
    "i": ("assets/tiles/rails/two_ways/turn/rails_up_right_vertical.png", "l"),

    "a": ("assets/tiles/rails/two_ways/straight/rails_horisontal_down_left.png", "q"),
    "s": ("assets/tiles/rails/two_ways/straight/rails_horisontal_down_right.png", "w"),
    "d": ("assets/tiles/rails/two_ways/straight/rails_horisontal_up_left.png", "e"),
    "f": ("assets/tiles/rails/two_ways/straight/rails_horisontal_up_right.png", "r"),

    "g": ("assets/tiles/rails/two_ways/straight/rails_vertical_down_left.png", "t"),
    "j": ("assets/tiles/rails/two_ways/straight/rails_vertical_down_right.png", "y"),
    "k": ("assets/tiles/rails/two_ways/straight/rails_vertical_up_left.png", "u"),
    "l": ("assets/tiles/rails/two_ways/straight/rails_vertical_up_right.png", "i")
}

TRAM_LOOKUP = {
    "u": ("assets/tram/tram_vertical.png", (0, -1)),
    "d": ("assets/tram/tram_vertical.png", (0, 1)),
    "l": ("assets/tram/tram_horisontal.png", (-1, 0)),
    "r": ("assets/tram/tram_horisontal.png", (1, 0)),
    "ul": ("assets/tram/tram_down_right.png", (-1, 1)),
    "ur": ("assets/tram/tram_down_left.png", (1, 1)),
    "dl": ("assets/tram/tram_down_left.png", (-1, -1)),
    "dr": ("assets/tram/tram_down_right.png", (1, -1))
}

MAP_ORDER = ["tutorial", "big_crossway", "prone_to_destruction", "test_1", "test_2"]
