import math


def dist(pos1, pos2):
    return abs(math.sqrt((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2))


def eval_all_edges_length(data):
    all_edges = []
    for i, first in enumerate(data):
        all_edges.append([])
        for j, second in enumerate(data):
            all_edges[i].append(dist(first, second))
    return all_edges
