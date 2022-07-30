from dataclasses import dataclass


@dataclass
class Config:
    display_height = 720
    display_width = 1280
    bullets_in_display = 5
    bullets_diameter = 3
    map_move_x_border_right = 896
    map_move_x_border_left = 100
    gravitation = 10


@dataclass
class Colors:
    SKY_BLUE = (161, 255, 254)
    BLUE = (5, 5, 180)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
