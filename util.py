import math
import random
import copy


def dist(pos1, pos2):
    return abs(math.sqrt((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2))


def eval_all_edges_length(data):
    all_edges = []
    for i, first in enumerate(data):
        all_edges.append([])
        for j, second in enumerate(data):
            all_edges[i].append(dist(first, second))
    return all_edges


def total_length(sequence, all_edges):
    total = 0
    for i, num in enumerate(sequence):
        if i is 0:
            total += all_edges[num][sequence[-1]]
        else:
            total += all_edges[num][sequence[i - 1]]
    return total


def find_neighbour(sequence, all_edges, current_total_distance, list_length):
    index1, index2 = random.sample(sequence, k=2)
    new_sequence = copy.deepcopy(sequence)
    new_total_distance = current_total_distance \
                         - all_edges[new_sequence[index1]][new_sequence[index1 - 1]] \
                         - all_edges[new_sequence[index1]][new_sequence[(index1 + 1) % list_length]] \
                         - all_edges[new_sequence[index2]][new_sequence[index2 - 1]] \
                         - all_edges[new_sequence[index2]][new_sequence[(index2 + 1) % list_length]] \
                         + all_edges[new_sequence[index1]][new_sequence[index2 - 1]] \
                         + all_edges[new_sequence[index1]][new_sequence[(index2 + 1) % list_length]] \
                         + all_edges[new_sequence[index2]][new_sequence[index1 - 1]] \
                         + all_edges[new_sequence[index2]][new_sequence[(index1 + 1) % list_length]]
    new_sequence[index1], new_sequence[index2] = new_sequence[index2], new_sequence[index1]
    return new_sequence, new_total_distance


def plot_graph(data, sequence, plt, camera):
    data_x = [_.x for _ in data]
    data_y = [_.y for _ in data]
    plt.scatter(data_x, data_y, c='#ff0000')
    for i, num in enumerate(sequence):
        if i is 0:
            plt.plot([data[sequence[0]].x, data[sequence[-1]].x], [data[sequence[0]].y, data[sequence[-1]].y])
        else:
            plt.plot([data[num].x, data[sequence[i - 1]].x], [data[num].y, data[sequence[i - 1]].y])
    camera.snap()


def acceptance(new, curr, t):
    if t is 0:
        return 0
    else:
        return math.exp((curr - new) / t)
