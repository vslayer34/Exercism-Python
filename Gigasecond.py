from helper import display_task_name, display_example

'''
Exersice: Gigasecond
URL: https://exercism.org/tracks/python/exercises/gigasecond

Instructions

Your task is to determine the date and time one gigasecond after a certain date.

A gigasecond is one thousand million seconds. That is a one with nine zeros after it.

If you were born on January 24th, 2015 at 22:00 (10:00:00pm), then you would be a gigasecond old on October 2nd, 2046 at 23:46:40 (11:46:40pm).
'''
from datetime import datetime, timedelta

def add(moment):
    giga_seconds = 1e9
    
    return moment + timedelta(seconds = giga_seconds)



display_task_name("I", "Gigasecond > date only specification of time")
display_example(
    "add(datetime(2011, 4, 25, 0, 0))",
    datetime(2043, 1, 1, 1, 46, 40)
    )
print(add(datetime(2011, 4, 25, 0, 0)))