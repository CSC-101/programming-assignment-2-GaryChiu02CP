from operator import truediv
from tarfile import TruncatedHeaderError

import data
from data import (Point, Duration, Song, Rectangle)

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(x:Point, y:Point) -> Rectangle: #takes two points, finds the top left and bottom rightmost values, and creates a rectangle with them
    if x.x < y.x:
        left = x.x
        right = y.x
    else:
        left = y.x
        right = x.x
    if x.y < y.y:
        bot = x.y
        top = y.y
    else:
        bot = y.y
        top = x.y
    rect = Rectangle(Point(left, top), Point(right, bot))
    return rect

# Part 2
def shorter_duration_than(d1:Duration,d2:Duration) -> bool: #takes 2 durations to check if the first is smaller than the other to return a boolean
    d1t = d1.minutes * 60 + d1.seconds
    d2t = d2.minutes * 60 + d2.seconds
    if d1t < d2t:
        return True
    else:
        return False

# Part 3
def song_shorter_than(array:list[Song], d:Duration) -> list[Song]: #takes a list of songs and a duration to output a list of songs whose duration is shorter than the given duration
    songlist = []
    for i in array:
        if i.duration.minutes*60+i.duration.seconds < d.minutes*60+d.seconds:
            songlist.append(i)
    return songlist

# Part 4
def running_time(songs:list[Song], x:list[int]) -> Duration: #takes a list of songs and ints. for each int in the list, index that from the songs and ad the duration to the total. return the total duration
    totalD = Duration(0,0)
    for i in x:
        totalD.minutes += songs[i].duration.minutes
        totalD.seconds += songs[i].duration.seconds
    totalD.minutes += totalD.seconds//60
    totalD.seconds = totalD.seconds%60
    return totalD

# Part 5
def validate_route(clinks:list[list[str]], route:list[str]) -> bool: #takes a list of city links and cities, checks whether a route is valid, and returns a boolean
    for i in range(len(route)-1):
        if [route[i],route[i+1]] not in clinks and [route[i+1],route[i]] not in clinks:
            return False
    return True

# Part 6
def longest_repetition(x:list[int]): #takes a list of integers and returns the index where the longest repetition begins or none if there are no repetitions
    longest_combo = 0
    combo = 0
    rep_i = None
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            combo += 1
            print(i, x[i], combo)
            if combo > longest_combo:
                rep_i = i-combo+1
                longest_combo = combo
        else:
            combo = 0
            print(i, x[i], combo)
    return rep_i