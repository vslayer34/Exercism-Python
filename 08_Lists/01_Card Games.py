"""
Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
https://exercism.org/tracks/python/exercises/card-games
"""


def get_rounds(number: int):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    list_of_rounds = []
    total_number_of_rounds = 3
    for i in range(0, total_number_of_rounds):
        list_of_rounds.append(number)
        number += 1
    return list_of_rounds

def concatenate_rounds(rounds_1: list, rounds_2: list):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2

def list_contains_round(rounds: list, number: int):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds


def card_average(hand: list):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    average = sum(hand) / len(hand)
    return average


def approx_average_is_average(hand: license):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    average_of_first_and_last = (hand[0] + hand[-1]) / 2
    index_of_meiddle_card = int(len(hand) / 2)
    value_of_the_middle_card = hand[index_of_meiddle_card]
    return index_of_meiddle_card


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    pass


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    pass



# Task I: Tracking Poker Rounds
# >>> get_rounds(27)
# [27, 28, 29]
print("Task I: Tracking Poker Rounds")
print(get_rounds(27), "\n")



# Task II: Keeping all Rounds in the Same Place
# >>> concatenate_rounds([27, 28, 29], [35, 36])
# [27, 28, 29, 35, 36]
print("Task II: Keeping all Rounds in the Same Place")
print(concatenate_rounds([27, 28, 29], [35, 36]), "\n")



# Task III: Finding Prior Rounds
print("Task III: Finding Prior Rounds")
# >>> list_contains_round([27, 28, 29, 35, 36], 29)
# True
print(list_contains_round([27, 28, 29, 35, 36], 29))

# >>> list_contains_round([27, 28, 29, 35, 36], 30)
# False
print(list_contains_round([27, 28, 29, 35, 36], 30), "\n")



# Task IV: Averaging Card Values
print("Task IV: Averaging Card Values")
# >>> card_average([5, 6, 7])
# 6.0
print(card_average([5, 6, 7]), "\n")



# Task V: Alternate Averages
print("Task V: Alternate Averages")
# >>> approx_average_is_average([1, 2, 3])
print(approx_average_is_average([1, 2, 3]))
# True

# >>> approx_average_is_average([2, 3, 4, 8, 8])
print(approx_average_is_average([2, 3, 4, 8, 8]))
# True

# >>> approx_average_is_average([1, 2, 3, 5, 9])
print(approx_average_is_average([1, 2, 3, 5, 9]), "\n")
# False



