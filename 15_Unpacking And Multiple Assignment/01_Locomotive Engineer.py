from helper import display_task_name, display_example

"""
Functions which helps the locomotive engineer to keep track of the train.
https://exercism.org/tracks/python/exercises/locomotive-engineer
"""


# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*args) -> list:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    # *list_of_args = *args

    return list(args)


# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id: list, missing_wagons: list) -> list:
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    correct_list = []

    first_index, second_index, id_one, *rest = each_wagons_id

    *correct_list, = id_one, *missing_wagons, *rest, first_index, second_index

    return correct_list


# TODO: define the 'add_missing_stops()' function
def add_missing_stops():
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    pass


# TODO: define the 'extend_route_information()' function
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    pass


# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[tuple] - the list of rows of wagons.
    :return: list[tuple] - list of rows of wagons.
    """
    pass



# Task 1
display_task_name("I", "Create a list of all wagons")
display_example(
    "get_list_of_wagons(1, 7, 12, 3, 14, 8, 5)",
    "[1, 7, 12, 3, 14, 8, 3]"
)
print(get_list_of_wagons(1, 7, 12, 3, 14, 8, 5), "\n")



# Task 2 
display_task_name("II", "Fix the list of wagons")
display_example(
    "fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])",
    "[1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]"
)
print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]), "\n")