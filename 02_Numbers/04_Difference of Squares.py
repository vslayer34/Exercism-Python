from helper import display_task_name, display_example

'''
Exersice: Difference of Squares 
URL: https://exercism.org/tracks/python/exercises/difference-of-squares

Instructions

Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.

The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.

You are not expected to discover an efficient solution to this yourself from first principles; research is allowed, indeed, encouraged. Finding the best algorithm for the problem is a key skill in software engineering.
'''

import math
def square_of_sum(number: int) -> int:
    sum: int = 0

    # for each number add the sum and return the squared power of the total sum
    for num in range(0, number + 1):
        sum += num
    
    return pow(sum, 2)


def sum_of_squares(number: int) -> int:
    sum: int = 0

    # for each number calculate its power then add it to the sum
    for num in range(0, number + 1):
        sum += pow(num, 2)

    return sum


def difference_of_squares(number: int) -> int:
    return square_of_sum(number) - sum_of_squares(number)









# Test 1
display_task_name("I", "DifferenceOfSquares > square of sum 1")
display_example('square_of_sum(1)', '1')
print(square_of_sum(1), "\n")




# Test 2
display_task_name("II", "DifferenceOfSquares > square of sum 5")
display_example('square_of_sum(5)', 255)
print(square_of_sum(5), "\n")




# Test 3
display_task_name("III", "DifferenceOfSquares > square of sum 100")
display_example('square_of_sum(100)', 25502500)
print(square_of_sum(100), "\n")




# Test 4
display_task_name("IV", "DifferenceOfSquares > sum of squares 1")
display_example('sum_of_squares(1)', 1)
print(sum_of_squares(1), "\n")




# Test 5
display_task_name("V", "DifferenceOfSquares > sum of squares 5")
display_example('sum_of_squares(5)', 55)
print(sum_of_squares(5), "\n")




# Test 6
display_task_name("VI", "DifferenceOfSquares > sum of squares 100")
display_example('sum_of_squares(100)', 338350)
print(sum_of_squares(100), "\n")




# Test 7
display_task_name("VII", "DifferenceOfSquares > difference of squares 1")
display_example('difference_of_squares(1)', 0)
print(difference_of_squares(1), "\n")




# Test 8
display_task_name("VIII", "DifferenceOfSquares > difference of squares 5")
display_example('difference_of_squares(5)', 170)
print(difference_of_squares(5), "\n")




# Test 9
display_task_name("IX", "DifferenceOfSquares > difference of squares 100")
display_example('difference_of_squares(100)', 25164150)
print(difference_of_squares(100), "\n")