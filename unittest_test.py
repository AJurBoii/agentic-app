import unittest

from main import bubble_sort, calculate_average, greet


class TestMain(unittest.TestCase):
    def test_greet(self):
        assert greet("AJ") == "Hello AJ!"
        assert greet("World") == "Hello World!"

    def test_bubble_sort(self):
        assert bubble_sort([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]
        assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
        assert bubble_sort([]) == []
        assert bubble_sort([42]) == [42]

    def test_calculate_average(self):
        assert calculate_average([10, 20, 30]) == 20.0
        assert calculate_average([5, 5, 5]) == 5.0


if __name__ == "__main__":
    unittest.main()
