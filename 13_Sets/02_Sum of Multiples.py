from helper import display_task_name, display_example

'''
Exersice Name: Sum of Multiples
URL: https://exercism.org/tracks/python/exercises/sum-of-multiples

Instructions

Given a number, find the sum of all the unique multiples of particular numbers up to but not including that number.

If we list all the natural numbers below 20 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18.

The sum of these multiples is 78.

You can make the following assumptions about the inputs to the sum_of_multiples function:

    All input numbers are non-negative ints, i.e. natural numbers including zero.
    A list of factors must be given, and its elements are unique and sorted in ascending order.

'''

def sum_of_multiples(limit: int, multiples: list) -> int:
    sum: int = 0

    for number in range(0, limit):
        for multiple in multiples:
            # prevent division by zero
            if multiple == 0:
                continue
            if number % multiple == 0:
                sum += number
                # break so each multiple is counted once
                break

    return sum


# print(sum_of_multiples(4, [3, 5]))

print(sum_of_multiples(10, [3, 5]))