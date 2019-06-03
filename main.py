import read_tsp_data
import random
import matplotlib.pyplot as plt

data = read_tsp_data.from_file('./data/ja9847.txt')
data_index = [_['index'] for _ in data]
data_x = [_['x'] for _ in data]
data_y = [_['y'] for _ in data]
plt.scatter(data_x, data_y, c='#ff0000')
plt.show()
