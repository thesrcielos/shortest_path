import logging, math
from twistedsort import constants


def split_and_sorted_approach(arr):
    if len(arr) == 0:
        return []
    odds = filter(lambda number: number % 2 == 1, arr)
    even = filter(lambda number: number % 2 == 0, arr)

    odds = sorted(odds, key=lambda x: -x)
    even = sorted(even)

    return even + odds


def no_split_and_sorted_approach(arr):
    if len(arr) == 0:
        return []
    return sorted(arr, key=lambda x: -x if x % 2 == 1 else x)


def full_sort_and_iterate_approach(arr):
    if len(arr) == 0:
        return []
    answer = []

    sorted_array = sorted(arr)
    for x in sorted_array:
        if x % 2 == 0:
            answer.append(x)

    reversed_sorted = sorted(arr, reverse=True)
    for x in reversed_sorted:
        answer.append(x)

    return answer

# There is another way to experimentally estimate the complexity of an algorithm
# This is by counting the elemental operations that the algorithm performs
# This could be a more precise way to estimate the complexity of an algorithm
# Take this function as an example for this approach
def split_and_sorted_approach_counting_elemental_operations(arr):
    elemental_operations = 0
    elemental_operations += 2
    n = len(arr)
    if len(arr) == 0:
        return []
    
    elemental_operations += 2*n
    odds = filter(lambda number: number % 2 == 1, arr)
    even = filter(lambda number: number % 2 == 0, arr)

    elemental_operations += 2*n*math.log(n, 2)
    odds = sorted(odds, key=lambda x: -x)
    even = sorted(even)
    elemental_operations += 2*n
    
    return even + odds, elemental_operations