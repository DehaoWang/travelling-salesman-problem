import read_tsp_data
from util import *
import random

data = read_tsp_data.from_file('./data/wi29.txt')
all_edges = eval_all_edges_length(data)
sequence = random.sample(range(0, len(data)), len(data))
current_total_distance = total_length(sequence, all_edges)
list_length = len(sequence)

print(f'Initial Sequence: {sequence}')
print(f'Initial Distance: {current_total_distance}')
plot_graph(data, sequence)

for t in range(5000, -1, -1):
    for i in range(10000):
        new_sequence, new_total_distance = find_neighbour(sequence, all_edges, current_total_distance, list_length)
        if new_total_distance < current_total_distance:
            sequence = new_sequence
            current_total_distance = new_total_distance
        elif acceptance(new_total_distance, current_total_distance, t) > random.uniform(0, 1):
            sequence = new_sequence
            current_total_distance = new_total_distance
    if t % 100 is 0:
        print(f"T: {t}")
        print(f'Best Sequence So Far: {sequence}')
        print(f'Shortest Distance So Far: {current_total_distance}')
    if t % 500 is 0:
        plot_graph(data, sequence)

# T: 0
# Best Sequence So Far:
# [1, 5, 9, 10, 14, 18, 17, 16, 20, 21, 22, 28, 27, 25, 19, 24, 26, 23, 15, 13, 12, 11, 7, 8, 6, 2, 3, 4, 0]
# Shortest Distance So Far: 28042.216388898618
