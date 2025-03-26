import pygame
from math import *


def center_distance(rect_a: pygame.Rect, rect_b: pygame.Rect) -> list[tuple[int, int] | int]:
    x_distance = int(rect_a.center[0] - rect_b.center[0])
    if x_distance > 0:
        x_sign = 1    #a to the right of b
    else:
        x_sign = -1  #b to the right of a
    x_distance = abs(x_distance)
    y_distance = int(rect_a.center[1] - rect_b.center[1])
    if y_distance > 0:  # if a is ABOVE b, y_sign is 1,if a is BELOW b, y_sign is -1!!
        y_sign = -1
    else:
        y_sign = 1
    y_distance = abs(y_distance)
    distance_total = int(ceil(sqrt(x_distance ** 2 + y_distance ** 2)))
    return [(x_sign, y_sign), (x_distance, y_distance), distance_total]
