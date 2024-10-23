from typing import Optional

import data
from data import Time
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



# Part 6
