import logging
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
    used = [False] * len(arr)
    sorted_array = sorted(arr)
    for x in sorted_array:
        if x % 2 == 0:
            answer.append(x)

    reversed_sorted = sorted(arr, reverse=True)
    for x in reversed_sorted:
        answer.append(x)

    return answer
