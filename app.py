import sys
from shortestpath import algorithms
from shortestpath import execution_time_gathering

if __name__ == "__main__":
    minimum_size = 40
    maximum_size = 200
    step = 20
    samples_by_size = 4
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Relations | Bellman Ford | Dijkstra | A*")
    for row in table:
        print(row)
