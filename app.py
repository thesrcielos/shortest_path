import sys
from twistedsort import algorithms
from twistedsort import execution_time_gathering

if __name__ == "__main__":
    minimum_size = 10000
    maximum_size = 100000
    step = 5000
    samples_by_size = 7
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Split and Sorted | No Split and Sorted | Full Sort and Iterate")
    for row in table:
        print(row)
