import sys
from twistedsort import algorithms
from twistedsort import execution_time_gathering

if __name__ == "__main__":
    table = execution_time_gathering.take_execution_time(1000, 10000, 500, 5)
    for row in table:
        print(row)
