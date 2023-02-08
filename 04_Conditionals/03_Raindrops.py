from helper import display_task_name, display_example
'''
Exercise Name: Raindrops
URL: https://exercism.org/tracks/python/exercises/raindrops

Instructions

Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if one number is a factor of another is to use the modulo operation.

The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.

Examples

    28 has 7 as a factor, but not 3 or 5, so the result would be "Plong".
    30 has both 3 and 5 as factors, but not 7, so the result would be "PlingPlang".
    34 is not factored by 3, 5, or 7, so the result would be "34".

'''


def convert(number: int) -> str:
    
    result: str = ""

    if number % 3 and number % 5 and number % 7 != 0:
        return str(number)

    if (number % 3) == 0:
        result += "Pling"
    
    if (number % 5) == 0:
        result += "Plang"
    
    if (number % 7) == 0:
        result += "Plong"
    

    return result



# Test 1
display_task_name("I", "Raindrops > the sound for 1 is 1")
display_example('convert(1)', '1')
print(convert(1), "\n")



# Tset 2
display_task_name("II", "Raindrops > the sound for 3 is pling")
display_example('convert(3)', 'Pling')
print(convert(3), "\n")



# Test 3
display_task_name("III", "Raindrops > the sound for 5 is plang")
display_example('convert(5)', 'Plang')
print(convert(5), "\n")



# Test 4
display_task_name("IV", "Raindrops > the sound for 7 is plong")
display_example('convert(7)', 'Plong')
print(convert(7), "\n")



# Test 5
display_task_name("V", "Raindrops > the sound for 6 is pling as it has a factor 3")
display_example('convert(6)', 'Pling')
print(convert(6), "\n")



# Test 6
display_task_name("VI", "Raindrops > 2 to the power 3 does not make a raindrop sound as 3 is the exponent not the base")
display_example('convert(8)', '8')
print(convert(8), "\n")



# Test 7
display_task_name("VII", "Raindrops > the sound for 9 is pling as it has a factor 3")
display_example('convert(9)', "Pling")
print(convert(9), "\n")



# Test 8
display_task_name("VIII", "Raindrops > the sound for 10 is plang as it has a factor 5")
display_example('convert(10)', 'Plang')
print(convert(10), "\n")



# Test 9
display_task_name("IX", "Raindrops > the sound for 14 is plong as it has a factor of 7")
display_example('convert(14)', 'Plong')
print(convert(14), "\n")



# Test 10
display_task_name("X", "Raindrops > the sound for 15 is pling plang as it has factors 3 and 5")
display_example('convert(15)', 'PlingPlang')
print(convert(15), "\n")



# Test 11
display_task_name("XI", "Raindrops > the sound for 21 is pling plong as it has factors 3 and 7")
display_example('convert(21)', 'PlingPlong')
print(convert(21), "\n")



# Test 12
display_task_name("XII", "Raindrops > the sound for 25 is plang as it has a factor 5")
display_example('convert(25)', 'Plang')
print(convert(25), "\n")



# Test 13
display_task_name("XIII", "Raindrops > the sound for 27 is pling as it has a factor 3")
display_example('convert(27)', 'Pling')
print(convert(27), "\n")



# Test 14
display_task_name("XIV", "Raindrops > the sound for 35 is plang plong as it has factors 5 and 7")
display_example('convert(35)', "PlangPlong")
print(convert(35), "\n")



# Test 15
display_task_name("XV", "Raindrops > the sound for 49 is plong as it has a factor 7")
display_example('convert(49)', "Plong")
print(convert(49), "\n")



# Test 16
display_task_name("XVI", "Raindrops > the sound for 52 is 52")
display_example('convert(52)', '52')
print(convert(52), "\n")



# Test 17
display_task_name("XVII", "Raindrops > the sound for 105 is pling plang plong as it has factors 3 5 and 7")
display_example('convert(105)', 'PlingPlangPLong')
print(convert(105), "\n")



# Test 18
display_task_name("XVIII", "Raindrops > the sound for 3125 is plang as it has a factor 5")
display_example('convert(3125)', 'convert(3125)')
print(convert(3125), "\n")