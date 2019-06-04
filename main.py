import read_tsp_data
from util import *
import random
import matplotlib.pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
data = read_tsp_data.from_file('./data/qa194.txt')
all_edges = eval_all_edges_length(data)
sequence = random.sample(range(0, len(data)), len(data))
current_total_distance = total_length(sequence, all_edges)
list_length = len(sequence)


def plot_graph():
    global data, sequence, camera
    data_x = [_.x for _ in data]
    data_y = [_.y for _ in data]
    plt.scatter(data_x, data_y, c='#ff0000')
    for i, num in enumerate(sequence):
        if i is 0:
            plt.plot([data[sequence[0]].x, data[sequence[-1]].x], [data[sequence[0]].y, data[sequence[-1]].y])
        else:
            plt.plot([data[num].x, data[sequence[i - 1]].x], [data[num].y, data[sequence[i - 1]].y])
    camera.snap()


print(f'Initial Sequence: {sequence}')
print(f'Initial Distance: {current_total_distance}')
plot_graph()

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
        plot_graph()

animation = camera.animate()
animation.save('qa194.mp4')

# Western Sahara - wi29.txt
# Best Sequence So Far:
# [1, 5, 9, 10, 14, 18, 17, 16, 20, 21, 22, 28, 27, 25, 19, 24, 26, 23, 15, 13, 12, 11, 7, 8, 6, 2, 3, 4, 0]
# Shortest Distance So Far: 28042.216388898618
# Optimal Tour: 27603

# Djibouti - dj38.txt
# Best Sequence So Far:
# [32, 33, 35, 30, 26, 27, 15, 11, 10, 16, 17, 18, 23, 21, 24, 25, 22, 19, 14, 12, 8, 7, 6, 5, 4, 2, 3, 1, 0, 9, 13, 20,
# 28, 29, 31, 34, 36, 37]
# Shortest Distance So Far: 6911.328307023829
# Optimal Tour: 6656

# Qatar - qa194.txt
# Best Sequence So Far:

# Shortest Distance So Far:
# Optimal Tour: 9352
