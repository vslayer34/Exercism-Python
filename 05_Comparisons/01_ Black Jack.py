"""
Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
https://exercism.org/tracks/python/exercises/black-jack
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    try:
        value_of_the_card = int(card)
        return value_of_the_card
    except:
        if (card is 'A'):
            return 1
        else:
            return 10


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)

    if value_of_card_one == value_of_card_two :
        return card_one, card_two
    elif value_of_card_one > value_of_card_two :
        return card_one
    else :
        return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # check if ace in the hand so that it can sumed = 11
    if card_one is 'A':
        card_one = '11'
    elif card_two is 'A':
        card_two = '11'
    # check if the total is more than 11 if so ace = 1 otherwise ace = 11
    if value_of_card(card_one) + value_of_card(card_two) >= 11 :
        return 1
    else :
        return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
     # check if ace in the hand so that it can sumed = 11
    if card_one is 'A':
        card_one = '11'
    elif card_two is 'A':
        card_two = '11'
    # check if the cards value == 21
    if value_of_card(card_one) + value_of_card(card_two) == 21:
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    # check if the value of the two cards are equal so they can be split
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    totals = [9, 10, 11]
    if (value_of_card(card_one) + value_of_card(card_two)) in totals:
        return True
    else:
        return False


# function 1 value_of_card(card)
# >>> value_of_card('K')
# 10
print(value_of_card('K'), '\n')

# >>> value_of_card('4')
# 4
print(value_of_card('4'), "\n")

# >>> value_of_card('A')
# 1
print(value_of_card('A'), "\n")


# function 2: higher_card(card_one, card_two)
# >>> higher_card('K', '10')
# ('K', '10')
print(higher_card('K', '10'), '\n')

# >>> higher_card('4', '6')
# '6'
print(higher_card('4', '6'), '\n')

# >>> higher_card('K', 'A')
# 'K'
print(higher_card('K', 'A'), '\n')



# fucntion 3: value_of_ace(card_one, card_two)
# >>> value_of_ace('6', 'K')
# 1
print(value_of_ace('6', 'K'), '\n')
# >>> value_of_ace('7', '3')
# 11
print(value_of_ace('7', '3'), '\n')



# function 4: is_blackjack(card_one, card_two)
# >>> is_blackjack('A', 'K')
# True
print(is_blackjack('A', 'K'), '\n')

# >>> is_blackjack('10', '9')
# False
print(is_blackjack('10', '9'), '\n')



# function 5: can_split_pairs(card_one, card_two)
# >>> can_split_pairs('Q', 'K')
# True
print(can_split_pairs('Q', 'K'), '\n')

# >>> can_split_pairs('10', 'A')
# False
print(can_split_pairs('10', 'A'), '\n')



# function 6: can_double_down(card_one, card_two)
# >>> can_double_down('A', '9')
# True
print(can_double_down('A', '9'), '\n')

# >>> can_double_down('10', '2')
# False
print(can_double_down('10', '2'), '\n')