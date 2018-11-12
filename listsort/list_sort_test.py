import unittest
from list_sort import list_sort

class Testlistsort(unittest.TestCase):
     def test_no_even(self):
        self.assertEqual(
            list_sort([9, 3, 5, 1, 'd', 'a']),
            {'evens': [], 'odds': [1, 3, 5, 9], 'chars': ['a', 'd']}
        )

     def test_no_odd(self):
        self.assertEqual(
            list_sort([10, 2, 8, 'c', 'f']),
            {'evens': [2, 8, 10], 'odds': [], 'chars': ['c', 'f']}
        )

     def test_complete_list(self):
        self.assertEqual(
            list_sort([4, 9, 2, 3, 5, 1, 'd', 'a', 'c', 'f']),
            {'evens': [2, 4], 'odds': [1, 3, 5, 9], 'chars': ['a', 'c', 'd', 'f']})


if __name__ == '__main__':
    unittest.main()