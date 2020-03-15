import unittest
from stalinSort import sort

class TestStalinSort(unittest.TestCase):

    def test_sort(self):
        result = sort([1,2,3,1,2,3,11,22,33,11,22,33,7,8,9,77,88,99])
        expected = [1,2,3,11,22,33,77,88,99]
        self.assertCountEqual(result, expected)

    def test_letters(self):
        result = sort(["a","b","c","a","b","c","x","y","z"])
        expected = ["a","b","c","x","y","z"]
        self.assertCountEqual(result, expected)

    def test_empty(self):
        result = sort([])
        expected = []
        self.assertCountEqual(result, expected)

    def test_numbers_and_letters(self):
        self.assertRaises(TypeError, sort, ["a","b","c",1,2,3,"a","b","c"])

    def test_null(self):
        self.assertRaises(TypeError, sort, None)

    # test to check if unittests work and fail correctly
    # def test_unittesting(self):
    #     self.assertRaises(TypeError, sum, [1,6])

if __name__ == "__main__":
    unittest.main()