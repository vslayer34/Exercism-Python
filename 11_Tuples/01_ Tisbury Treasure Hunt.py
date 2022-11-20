from helper import display_example, display_task_name

"""
Functions to help Azara and Rui locate pirate treasure.
https://exercism.org/tracks/python/exercises/tisbury-treasure-hunt
"""


def get_coordinate(record: tuple):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]


def convert_coordinate(coordinate: str):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)


def compare_records(azara_record: tuple, rui_record: tuple):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    second_coordinate = ""
    for character in rui_record[1]:
        second_coordinate += character
    
    return azara_record[1] == second_coordinate


def create_record(azara_record: tuple, rui_record: tuple):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return "not a match"


def clean_up(combined_record_group: tuple):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    all_tules = ""
    for single_tuple in combined_record_group:
        new_tuple = single_tuple[:1] + single_tuple[2:]
        all_tules += f"{new_tuple}\n"
    return all_tules



# Task 1
display_task_name("I", "Extract coordinates")
display_example(
    "get_coordinate(('Scrimshawed Whale Tooth', '2A'))", 
    "2A"
)
print(get_coordinate(('Scrimshawed Whale Tooth', '2A')), "\n")



# Task 2
display_task_name("II", "Format coordinates")
display_example(
    'convert_coordinate("2A")',
    '("2", "A")'
    )

print(convert_coordinate("2A"), "\n")



# Task 3
display_task_name("III", "Match coordinates")
display_example(
    "compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue'))",
    "False"
)

print(compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')), "\n")

display_example(
    "compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple'))", 
    "True"
)

print(compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple')), "\n")



# Task 4
display_task_name("IV", "Combine matched records")

display_example(
    "create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))", 
    "('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')"
)
print(create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue')), "\n")

display_example(
    "create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue'))", 
    "not a match"
)
print(create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')), "\n")



# Task 5
display_task_name('V', '"Clean up" & make a report of all records')
display_example(
    "clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')))", 
    """
    ('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')
    ('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')
    ('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')
    """
)
print(clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))), "\n")