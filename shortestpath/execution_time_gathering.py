import time

from shortestpath import algorithms
from shortestpath import constants
from shortestpath import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size):
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_graph(size))

    sample1 = take_time_for_algorithm(samples, algorithms.bellman_ford)
    return [
        sample1[0],
        sample1[1],
        take_time_for_algorithm(samples, algorithms.dijkstra)[1],
        take_time_for_algorithm(samples, algorithms.a_star)[1],
    ]


"""
    Returns the median of the execution time measures for a sorting approach given in 
"""


def take_time_for_algorithm(samples_array, shortest_approach):
    times = []
    m = 0
    for sample in samples_array:
        graph, start, goal, m = sample
        start_time = time.time()
        shortest_approach(graph, start, goal)
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return [m, times[len(times) // 2]]
