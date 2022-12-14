# function for displaying the output and the examples
from helper import display_example, display_task_name

"""
Functions to manage and organize queues at Chaitana's roller coaster.
https://exercism.org/tracks/python/exercises/chaitanas-colossal-coaster
"""


def add_me_to_the_queue(express_queue: list, normal_queue: list, ticket_type: int, person_name: str):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    exprss_code = 1
    normal_code = 0
    if ticket_type == exprss_code:
        express_queue.append(person_name)
        return express_queue

    elif ticket_type == normal_code:
        normal_queue.append(person_name)
        return normal_queue
    else:
        return ValueError(ticket_type, "is not correct either 1 for express or 0 for normal")


def find_my_friend(queue: list, friend_name: str):
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list, index: int, person_name: str):
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list, person_name: str):
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list, person_name: str):
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """
    return queue.count(person_name)


def remove_the_last_person(queue: list):
    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    return queue.pop()


def sorted_names(queue: list):
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    return sorted(queue)


# Task I
display_task_name("I", "Add me to the queue")
display_example('add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich")'
    ,["Tony", "Bruce", "RichieRich"])
print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich"), "\n")


display_example('add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye")'
    ,["RobotGuy", "WW", "HawkEye"])
print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye"), "\n")



# Task II
display_task_name("II", "Where are my friends?")

display_example('find_my_friend(queue=["Natasha", "Steve", "T\'challa", "Wanda", "Rocket"], friend_name="Steve")', "1")
print(find_my_friend(queue=["Natasha", "Steve", "T\'challa", "Wanda", "Rocket"], friend_name="Steve"), "\n")



# Task III
display_task_name("III", "Can I please join them?")

display_example('add_me_with_my_friends(queue=["Natasha", "Steve", "T\'challa", "Wanda", "Rocket"], index=1, person_name="Bucky")'
    , '["Natasha", "Bucky", "Steve", "T\'challa", "Wanda", "Rocket"]')
print(add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky"), "\n")



# Task IV
display_task_name("IV", "Mean person in the queue")
display_example('remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran")'
    , '["Natasha", "Steve", "Wanda", "Rocket"]')
print(remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran"), "\n")



# Task V
display_task_name("V", "Namefellows")
display_example('how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha")', '2')
print(how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha"), "\n")



# Task VI
display_task_name("VI", "Remove the last person")
display_example('remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])', 'Rocket')
print(remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]), "\n")




# Task VII
display_task_name("VII", "Sort the Queue List")
display_example('sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])', "['Eltran', 'Natasha', 'Natasha', 'Rocket', 'Steve']")
print(sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]), "\n")