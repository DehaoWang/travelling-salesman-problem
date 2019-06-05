# Travelling Salesman Problem
This project aims at obtaining sub-optimal solutions to the famous [Travelling Salesman Problem (TSP)](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (assuming distances satisfy triangle inequality) with one of the [Monte Carlo methods](https://en.wikipedia.org/wiki/Monte_Carlo_method) called [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing).

## Results
The solutions found for the different data sets are show below (updated whenever new results come out).

You can also find the [suggested optimal tours](http://www.math.uwaterloo.ca/tsp/world/countries.html#WI) for different data sets in the link.

The optimal results found here might have some difference from the suggested optimal tour on the website. The reason is being the round off errors in the distance formula.

You can double check the path in the animation against the optimal tour path shown on the website.

### wi29 (Western Sahara)
Below is the animation for the optimal solution found for the data set [**wi29**](http://www.math.uwaterloo.ca/tsp/world/wi29.tsp) (based on real world location data of **29 cities** in **Western Sahara**):

![Western Sahara(optimal)](wi29(27748).gif)

*(Initial temperature = 5000, epochs = 1000)*

The optimal distance found is **27748.70957813486** (compared to [suggested optimal solution of 27603](http://www.math.uwaterloo.ca/tsp/world/witour.html)).

### dj38 (Djibouti)
Below is the animation for the optimal solution found for the data set [**dj38**](http://www.math.uwaterloo.ca/tsp/world/dj38.tsp) (based on real world location data of **38 cities** in **Djibouti**, a country in East Africa):

![Djibouti(optimal)](dj38(6659).gif)

*(Initial temperature = 5000, epochs = 1000)*

The optimal distance found is **6659.431532931465** (compared to [suggested optimal solution of 6656](http://www.math.uwaterloo.ca/tsp/world/djtour.html)).

### dj38 (Djibouti) - sub-optimal result
Since Simulated Annealing is a probabilistic approach, there is times that you can only find an almost-optimal (sub-optimal) solution.

Here's an example:

![Djibouti](dj38(6911).gif)

*(Initial temperature = 5000, epochs = 10000)*

The above sub-optimal solution has total distance of **6911** (about **1%** away from optimal solution).

## Data used in this program
All data sets are taken from the [TSP website of Math Department in University of Waterloo](http://www.math.uwaterloo.ca/tsp/world/countries.html#DJ).

## Description
The program reads and convert real-world location data from the TSP data taken from the aforementioned website above.

- Note: index of location data are 1-based and the converted data are 0-based for ease of programming.

The main point of entrance is **main.py**, and **read_tsp_data.py** helps read the data. **util.py** is a collection of the utility functions used in the program.

The simulation gradually runs from **T = 5000** (or other initial temperature) to **T = 0** with steps of 1. At each temperature, **10,000 epochs** (depending on the data set size) are run.

- Some of the best output results are manually stored in results.txt, and the indexes of cities in the sequence are also 0-based (add 1 to get back their corresponding number in the original TSP data).

## Software
- Python 3.7
- Matplotlib (for graph plotting)
- [Celluloid](https://github.com/jwkvam/celluloid) (for animation)
- [FFmpeg](https://ffmpeg.org/) (for animation)

## Credits
The algorithm written in this program is inspired by this [Youtube video](https://www.youtube.com/watch?v=eBmU1ONJ-os&t=1s) which explains how Simulated Annealing works.