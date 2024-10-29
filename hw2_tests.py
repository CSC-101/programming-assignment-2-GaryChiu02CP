from unittest import expectedFailure

import data
import hw2
import unittest

import hw2_tests
from data import Point, Rectangle, Duration, Song
from hw2 import song_shorter_than, validate_route


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        x = Point(2,2)
        y = Point(10,10)
        expected = Rectangle(Point(2,10),Point(10,2))
        result = hw2.create_rectangle(x,y)
        self.assertEqual(expected,result)

    def test_create_rectangle_2(self):
        x = Point(10, 7)
        y = Point(14, 7)
        expected = Rectangle(Point(10, 7), Point(14, 7))
        result = hw2.create_rectangle(x, y)
        self.assertEqual(expected, result)

    # Part 2
    def test_shorter_duration_than_1(self):
        d1 = Duration(50,20)
        d2 = Duration(49,30)
        expected = False
        result = hw2.shorter_duration_than(d1,d2)
        self.assertEqual(expected,result)

    def test_shorter_duration_than_2(self):
        d1 = Duration(50, 20)
        d2 = Duration(50, 30)
        expected = True
        result = hw2.shorter_duration_than(d1, d2)
        self.assertEqual(expected, result)

    # Part 3
    def test_songs_shorter_than_1(self):
        s1 = Song("al","One",Duration(4,41))
        s2 = Song("al","Two",Duration(3,54))
        s3 = Song("al","Three",Duration(3,101))
        array = [s1,s2,s3]
        d = Duration(4,40)
        expected = [s2]
        result = song_shorter_than(array,d)
        self.assertEqual(expected,result)

    def test_songs_shorter_than_2(self):
        s1 = Song("al", "amish", Duration(3, 50))
        s2 = Song("al", "butter", Duration(2, 60))
        s3 = Song("al", "house", Duration(3, 40))
        array = [s1,s2,s3]
        d = Duration(3, 50)
        expected = [s2,s3]
        result = song_shorter_than(array, d)
        self.assertEqual(expected, result)

    # Part 4
    def test_running_time_1(self):
        s1 = Song("al", "One", Duration(4, 41))
        s2 = Song("al", "Two", Duration(3, 54))
        s3 = Song("al", "Three", Duration(4, 41))
        s4 = Song("al", "amish", Duration(3, 50))
        s5 = Song("al", "butter", Duration(3, 00))
        s6 = Song("al", "house", Duration(3, 40))
        array = [s1,s2,s3,s4,s5,s6]
        indexes = [4,4,4,4]
        expected = Duration(12,00)
        result = hw2.running_time(array, indexes)
        self.assertEqual(expected, result)

    def test_running_time_2(self):
        s1 = Song("al", "One", Duration(4, 41))
        s2 = Song("al", "Two", Duration(3, 54))
        s3 = Song("al", "Three", Duration(4, 41))
        s4 = Song("al", "amish", Duration(3, 50))
        s5 = Song("al", "butter", Duration(3, 00))
        s6 = Song("al", "house", Duration(3, 40))
        array = [s1, s2, s3, s4, s5, s6]
        indexes = [5,4,3]
        expected = Duration(10, 30)
        result = hw2.running_time(array, indexes)
        self.assertEqual(expected, result)

    # Part 5
    def test_validate_route_1(self):
        clinks = [
                ['san luis obispo', 'santa margarita'],
                ['san luis obispo', 'pismo beach'],
                ['atascadero', 'santa margarita'],
                ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'santa margarita', 'atascadero', 'creston', 'atascadero', 'santa margarita']
        expected = True
        result = validate_route(clinks, route)
        self.assertEqual(expected,result)

    def test_validate_route_2(self):
        clinks = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'santa margarita', 'pismo beach', 'atascadero']
        expected = False
        result = validate_route(clinks, route)
        self.assertEqual(expected, result)

    def test_validate_route_3(self):
        clinks = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = []
        expected = True
        result = validate_route(clinks, route)
        self.assertEqual(expected, result)

    def test_validate_route_4(self):
        clinks = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo']
        expected = True
        result = validate_route(clinks, route)
        self.assertEqual(expected, result)

    # Part 6
    def test_longest_repetition_1(self):
        array = [1, 1, 2, 2, 1, 1, 1, 3,9,1,1,1,1]
        expected = 9
        result = hw2.longest_repetition(array)
        self.assertEqual(expected, result)

    def test_longest_repetition_2(self):
        array = [1,2,1,1,1,1,2,3,1,1,1,1]
        expected = 2
        result = hw2.longest_repetition(array)
        self.assertEqual(expected, result)

    def test_longest_repetition_3(self):
        array = [1,2,3,4,5,6,7,8,9]
        expected = None
        result = hw2.longest_repetition(array)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
