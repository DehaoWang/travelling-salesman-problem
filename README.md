# Travelling Salesman Problem
This project aims at obtaining sub-optimal solutions to the famous [Travelling Salesman Problem (TSP)](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (assuming distances satisfy triangle inequality) with one of the [Monte Carlo methods](https://en.wikipedia.org/wiki/Monte_Carlo_method) called [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing).

Below is an animation generated from one of the simulations (data based on real world location data of **38 cities** in **Djibouti**, a country in East Africa):

![Djibouti](dj38(6911).gif)

The above simulation is a sub-optimal solution of the problem with total distance of **6911** (about **1%** away from optimal solution).

You can check out the suggested optimal solution [here](http://www.math.uwaterloo.ca/tsp/world/djtour.html) which has a total distance of **6656**.

## Data used in this program
All data sets are taken from the [TSP website of Math Department in University of Waterloo](http://www.math.uwaterloo.ca/tsp/world/countries.html#DJ).

## Description
The program reads and convert real-world location data from the TSP data taken from the aforementioned website above.

- Note: index of location data are 1-based and the converted data are 0-based for ease of programming.

The main point of entrance is **main.py**, and **read_tsp_data.py** helps read the data. **util.py** is a collection of the utility functions used in the program.

The simulation gradually runs from **T = 5000** to **T = 0** with steps of 1. At each temperature, **10,000 epochs** are run.

- Some of the best output results are manually stored in results.txt, and the indexes of cities in the sequence are also 0-based (add 1 to get back their corresponding number in the original TSP data).

## Software
- Python 3.7
- Matplotlib (for graph plotting)
- [Celluloid](https://github.com/jwkvam/celluloid) (for animation)
- [FFmpeg](https://ffmpeg.org/) (for animation)

## Credits
The algorithm written in this program is inspired by this [Youtube video](https://www.youtube.com/watch?v=eBmU1ONJ-os&t=1s) which explains how Simulated Annealing works.