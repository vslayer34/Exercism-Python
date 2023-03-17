from helper import display_task_name, display_example
'''
Exersice Name: Perfect Numbers
URL: https://exercism.org/tracks/python/exercises/perfect-numbers

Instructions

Determine if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.

The Greek mathematician Nicomachus devised a classification scheme for positive integers, identifying each as belonging uniquely to the categories of perfect, abundant, or deficient based on their aliquot sum. The aliquot sum is defined as the sum of the factors of a number not including the number itself. For example, the aliquot sum of 15 is (1 + 3 + 5) = 9

    Perfect: aliquot sum = number
        6 is a perfect number because (1 + 2 + 3) = 6
        28 is a perfect number because (1 + 2 + 4 + 7 + 14) = 28
    Abundant: aliquot sum > number
        12 is an abundant number because (1 + 2 + 3 + 4 + 6) = 16
        24 is an abundant number because (1 + 2 + 3 + 4 + 6 + 8 + 12) = 36
    Deficient: aliquot sum < number
        8 is a deficient number because (1 + 2 + 4) = 7
        Prime numbers are deficient

Implement a way to determine whether a given number is perfect. Depending on your language track, you may also need to implement a way to determine whether a given number is abundant or deficient.
'''

def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # sum of the total numbers
    sum: int = 0

    # raise an error if the number is negative
    if (number <= 0):
        raise ValueError("Classification is only possible for positive integers.")
    
    # see all numbers before the target number
    # and divide by that's number to get the factors
    for num in range(1, number):
        if number % num == 0:
            sum += num
    
    if (sum == number):
        return "perfect"
    elif (sum > number):
        return "abundant"
    else:
        return "deficient"


# Test 1
display_task_name("I", "PerfectNumbers > smallest perfect number is classified correctly")
display_example("classify(6)", "perfect")
print(classify(6), '\n')