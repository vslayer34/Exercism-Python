from helper import display_task_name, display_example
import math
'''
URL: https://exercism.org/tracks/python/exercises/armstrong-numbers

Instructions

An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

For example:

    9 is an Armstrong number, because 9 = 9^1 = 9
    10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
    153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

Write some code to determine whether a number is an Armstrong number.

'''


def is_armstrong_number(number: int) -> bool:
    # Convert the number to a list to iterate through it
    list_of_number = [ int(num) for num in str(number) ]

    sum = 0
    
    # Go through each number in the list and power it to the number of digits
    # then adding ther sumation
    for num in list_of_number:
        sum += pow(num, len(list_of_number))
    

    return sum == number






# Test 1
display_task_name("I", "ArmstrongNumbers > zero is an armstrong number")
display_example(
    "is_armstrong_number(0)",
    "True"
)
print(is_armstrong_number(0), "\n")



# Test 2
display_task_name("II", "ArmstrongNumbers > single digit numbers are armstrong numbers")
display_example(
    "is_armstrong_number(5)",
    "True"
)
print(is_armstrong_number(5), "\n")



# Test 3
display_task_name("III", "ArmstrongNumbers > there are no two digit armstrong numbers")
display_example(
    "is_armstrong_number(10)",
    "False"
)
print(is_armstrong_number(10), "\n")



# Test 4
display_task_name("IV", "ArmstrongNumbers > three digit number that is an armstrong number")
display_example(
    "is_armstrong_number(153)",
    "True"
)
print(is_armstrong_number(153), "\n")



# Test 5
display_task_name("V", "ArmstrongNumbers > three digit number that is not an armstrong number")
display_example(
    "is_armstrong_number(100)",
    "False"
)
print(is_armstrong_number(100), "\n")



# Test 6
display_task_name("VI", "ArmstrongNumbers > four digit number that is an armstrong number")
display_example(
    "is_armstrong_number(9474)",
    "True"
)
print(is_armstrong_number(9474), "\n")



# Test 7
display_task_name("VII", "ArmstrongNumbers > four digit number that is not an armstrong number")
display_example(
    "is_armstrong_number(9475)",
    "False"
)
print(is_armstrong_number(9475), "\n")



# Test 8
display_task_name("VIII", "ArmstrongNumbers > seven digit number that is an armstrong number")
display_example(
    "is_armstrong_number(9926315)",
    "True"
)
print(is_armstrong_number(9926315), "\n")



# Test 9
display_task_name("IX", "ArmstrongNumbers > seven digit number that is not an armstrong number")
display_example(
    "is_armstrong_number(9926314)",
    "False"
)
print(is_armstrong_number(9926314), "\n")