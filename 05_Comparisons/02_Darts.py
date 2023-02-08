from helper import display_task_name, display_example
'''
Darts
URL: https://exercism.org/tracks/python/exercises/darts

Instructions

Write a function that returns the earned points in a single toss of a Darts game.

Darts is a game where players throw darts at a target.

In our particular instance of the game, the target rewards 4 different amounts of points, depending on where the dart lands:

    If the dart lands outside the target, player earns no points (0 points).
    If the dart lands in the outer circle of the target, player earns 1 point.
    If the dart lands in the middle circle of the target, player earns 5 points.
    If the dart lands in the inner circle of the target, player earns 10 points.

The outer circle has a radius of 10 units (this is equivalent to the total radius for the entire target), the middle circle a radius of 5 units, and the inner circle a radius of 1. Of course, they are all centered at the same point (that is, the circles are concentric defined by the coordinates (0, 0).

Write a function that given a point in the target (defined by its Cartesian coordinates x and y, where x and y are real), returns the correct amount earned by a dart landing at that point.
'''

import math
def score(x: float, y: float) -> int:
    # inner circle radius is 1 point
    inner_circle_radius_squared = math.pow(1, 2)

    # middle circle radius is 5 point
    middle_circle_radius_squared = math.pow(5, 2)

    # outer circle radius is 10 point
    outer_circle_radius_squared = math.pow(10, 2)

    # get the distance squared using the two points from Pythagorean theorem
    pythagorean_theorem = math.pow(x - 0, 2) + math.pow(y - 0, 2)

    # if out of the outer circle
    if pythagorean_theorem > outer_circle_radius_squared:
        return 0
    elif pythagorean_theorem <= inner_circle_radius_squared:
        return 10
    elif pythagorean_theorem <= middle_circle_radius_squared:
        return 5
    elif pythagorean_theorem <= outer_circle_radius_squared:
        return 1




# Test 1
display_task_name("I", "Darts > missed target")
display_example('score(-9, 9)', 0)
print(score(-9, 9), "\n")



# Test 2
display_task_name("II", "Darts > on the outer circle")
display_example('score(0, 10)', 1)
print(score(0, 10), "\n")



# Test 3
display_task_name("III", "Darts > on the middle circle")
display_example('score(-5, 0)', 5)
print(score(-5, 0), "\n")



# Test 4
display_task_name("IV", "Darts > on the inner circle")
display_example('score(0, -1)', 10)
print(score(0, -1), "\n")



# Test 5
display_task_name("V", "Darts > exactly on centre")
display_example('score(0, 0)', 10)
print(score(0, 0), "\n")



# Test 6
display_task_name("VI", "Darts > near the centre")
display_example('score(-0.1, -0.1)', 10)
print(score(-0.1, -0.1), "\n")



# Test 7
display_task_name("VII", "Darts > just within the inner circle")
display_example('score(0.7, 0.7)', 10)
print(score(0.7, 0.7), "\n")



# Test 8
display_task_name("VIII", "Darts > just outside the inner circle")
display_example('score(0.8, -0.8)', 5)
print(score(0.8, -0.8), "\n")



# Test 9
display_task_name("IX", "Darts > just within the middle circle")
display_example('score(-3.5, 3.5)', 5)
print(score(-3.5, 3.5), "\n")



# Test 10
display_task_name("X", "Darts > just outside the middle circle")
display_example('score(-3.6, -3.6)', 1)
print(score(-3.6, -3.6), "\n")



# Test 11
display_task_name("XI", "Darts > just within the outer circle")
display_example('score(-7.0, 7.0)', 1)
print(score(-7.0, 7.0), "\n")



# Test 12
display_task_name("XII", "Darts > just outside the outer circle")
display_example('score(7.1, -7.1)', 0)
print(score(7.1, -7.1), "\n")



# Test 13
display_task_name("XIII", "Darts > asymmetric position between the inner and middle circles")
display_example('score(0.5, -4)', 5)
print(score(0.5, -4), "\n")


