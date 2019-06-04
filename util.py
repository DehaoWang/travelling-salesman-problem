import math, random, copy


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
    index = random.randint(0, len(sequence) - 1)
    new_sequence = copy.deepcopy(sequence)
    new_total_distance = current_total_distance \
                         - all_edges[new_sequence[index - 1]][new_sequence[index - 2]] \
                         - all_edges[new_sequence[index]][new_sequence[(index + 1) % list_length]] \
                         + all_edges[new_sequence[index]][new_sequence[index - 2]] \
                         + all_edges[new_sequence[index - 1]][new_sequence[(index + 1) % list_length]]
    new_sequence[index], new_sequence[index - 1] = new_sequence[index - 1], new_sequence[index]
    return new_sequence, new_total_distance


def acceptance(new, curr, t):
    if t is 0:
        return 0
    else:
        return math.exp((curr - new) / t)
