'''
Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

There once was a wise servant who saved the life of a prince. The king promised to pay whatever the servant could dream up. Knowing that the king loved chess, the servant told the king he would like to have grains of wheat. One grain on the first square of a chess board, with the number of grains doubling on each successive square.

There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, and so on).
'''

# how many grains were on a given square
import re


def square(number):
    # number of grain at the first index
    number_of_grains = 1
    # check if the number is between 1 and 64
    if (number > 64 or number < 1):
        raise ValueError("square must be between 1 and 64")

    # check if the number isn't int
    if (type(number) is not int):
        raise TypeError("The number must be of type int")

    # square 1 should always have 1 grain
    if (number == 1):
        return number_of_grains
    
    # for everu successive square is multiplied by two number of times equal number of square - 1
    else:
        for i in range(0, number - 1) :
            number_of_grains *= 2
        return number_of_grains


# the total number of grains on the chessboard
def total():
    # initial sum of grains
    sum = 0
    for i in range(1, 65):
        sum += square(i)
    return sum




# Test 1
# grains on square 1 should return 1
print(square(1))

# Test 2
# grains on square 2 should return 2
print(square(2))

# Test 3
# grains on square 3 should return 4
print(square(3))

# Test 4
# grains on square 4 should return 8
print(square(4))

# Test 5
# grains on square 16 should return 32768
print(square(16))

# Test 6
# grains on square 32 should return 2147483648
print(square(32))

# Test 7
# grains on square 64 should return 9223372036854775808
print(square(64))


# Test 10
# total number of grains on the board should return 18446744073709551615
print(total())