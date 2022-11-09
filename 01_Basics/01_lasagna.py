"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(lasagna_in_oven):
    return EXPECTED_BAKE_TIME - lasagna_in_oven
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the total preparation time.
    :param layer: int number of layers.
    :return: int total time of preparation for all layers.
    Function that takes a number of lasagna layers, and returns how many minutes
    it needs to be prepared, based on the `TIME_PER_LAYER`.
    """
    return number_of_layers * PREPARATION_TIME


# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the full time needed (preparation + baking) in minutes.
    :param layer: int number of layers.
    :param baking_time: total baking time needed in minutes.
    :return: int total time in minutes to prepare and bake the marvellous lasagna.
    Function that takes the preparation and baking times, and return the total in
    minutes.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)

print(bake_time_remaining(30))
print(preparation_time_in_minutes(2))
print(elapsed_time_in_minutes(1, 3))