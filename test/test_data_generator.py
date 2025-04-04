import unittest
from shortestpath import data_generator
from shortestpath import constants
from shortestpath.data_generator import bfs_path

class DataGeneratorTest(unittest.TestCase):
    def test_data_generator_with_empty_list(self):
        N = 0
        random_list = data_generator.get_random_graph(N)
        self.assertTrue(N == len(random_list))
        pass

    def test_data_generator_with_1(self):
        N = 1
        random_list = data_generator.get_random_graph(N)
        self.assertTrue(N == len(random_list[0]))
        pass

    def test_data_generator_with_2(self):
        N = 2
        random_list = data_generator.get_random_graph(N)
        self.assertTrue(N == len(random_list[0]))
        self.assertTrue(random_list[1] != random_list[2])
        pass

    def test_data_generator_with_100(self):
        N = 100
        random_list = data_generator.get_random_graph(N)
        self.assertTrue(N == len(random_list[0]))
        for number in random_list[0]:
            for number, b in number:
                self.assertTrue(number < N)
                self.assertTrue(b >= 0)
        pass

    def test_data_generator_has_always_a_path(self):
        N = 100
        for i in range(10):
            data = data_generator.get_random_graph(N)
            self.assertTrue(bfs_path(data[0], data[1], data[2], constants.MAX_VALUE))
        pass


if __name__ == "__main__":
    unittest.main()
