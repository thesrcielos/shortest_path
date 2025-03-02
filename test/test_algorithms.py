import unittest
from shortestpath import algorithms
from shortestpath import data_generator
from shortestpath import constants

tests_input = [
    (
        [
            [(1, 1), (2, 4)],
            [(0, 1), (2, 2), (3, 5)],
            [(0, 4), (1, 2), (3, 1)],
            [(1, 5), (2, 1)]
        ],
        0,  
        3   
    ),  
    (
        [
            [(1, 10), (2, 3)],
            [(0, 10), (2, 1), (3, 2)],
            [(0, 3), (1, 1), (3, 8), (4, 4)],
            [(1, 2), (2, 8), (4, 7)],
            [(2, 4), (3, 7)]
        ],
        0,  
        4   
    ),  
    (
        [
            [(1, 7), (2, 9), (5, 14)],
            [(0, 7), (2, 10), (3, 15)],
            [(0, 9), (1, 10), (3, 11), (5, 2)],
            [(1, 15), (2, 11), (4, 6)],
            [(3, 6), (5, 9)],
            [(0, 14), (2, 2), (4, 9)]
        ],
        0,  
        4   
    )
]

tests_output = [
    [0, 1, 2, 3],  
    [0, 2, 4],  
    [0, 2, 5, 4]  
]


class AlgorithmsTests(unittest.TestCase):
    def test_bellman_ford(self):
        for i in range(len(tests_input)):
            array, start, goal = tests_input[i]
            result = algorithms.bellman_ford(array, start, goal)
            self.assertEqual(result, tests_output[i])

    def test_dijkstra(self):
        for i in range(len(tests_input)):
            array, start, goal = tests_input[i]
            result = algorithms.dijkstra(array, start, goal)
            self.assertEqual(result, tests_output[i])

    def test_a_star(self):
        for i in range(len(tests_input)):
            array, start, goal = tests_input[i]
            result = algorithms.a_star(array, start, goal)
            self.assertEqual(result, tests_output[i])


if __name__ == "__main__":
    unittest.main()
