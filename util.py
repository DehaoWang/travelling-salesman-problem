import math


def dist(pos1, pos2):
    return abs(math.sqrt((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2))
