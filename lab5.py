from typing import Optional
from math import sqrt
import data
from data import Time, Point
# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1:Time, time2:Time) -> Time:
    #initializes an output
    output_time = Time(0,0,0)
    #adds the seconds and take the remainder from 60, push the excess to carry
    output_time.second = (time1.second + time2.second) % 60
    carry_seconds = (time1.second + time2.second) // 60
    #adds the minutes and take the remainder from 60, push the excess to carry
    output_time.minute = (time1.minute + time2.minute + carry_seconds) % 60
    carry_minutes = (time1.minute + time2.minute + carry_seconds) // 60
    #adds the hours and carry
    output_time.hour = time1.hour + time2.hour + carry_minutes
    return output_time

# Part 4
def is_descending(input_list:list[float]) -> bool:
    for n in range(len(input_list) - 1):
        if input_list[n+1] >= input_list[n]:
            return False
    return True

# Part 5
def largest_between(input_list:list[int], lower:int, upper:int) -> Optional[int]:
    largest = 0
    if upper < lower:
        return None
    for n in range(lower,(upper+1)):
        if input_list[n] > largest:
            largest = input_list[n]
    return largest

list_a = [40, 10, 15, 5, 20, 35]

# Part 6

def distance(point_a: Point, point_b: Point) -> float:
    length = abs(point_a.x - point_b.x)
    height = abs(point_a.y - point_b.y)
    return sqrt((length ** 2) +
                (height ** 2))
def furthest_from_origin(point_list:list[Point]) -> Optional[int]:
    if point_list == []:
        return None
    distance_list = []
    for n in point_list:
        distance_list.append(distance(n, Point(0,0)))
    highest_distance = 0
    highest_idx = 0
    for n in range(len(distance_list) -1):
        if distance_list[n] > highest_distance:
            highest_distance = distance_list[n]
            highest_idx = n
    return highest_idx


list_b = [Point(4,2), Point(6, 10), Point(-2, 17), Point(-70, 80), Point(10, 19)]
