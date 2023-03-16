from helper import display_task_name, display_example

'''
Exersice:  Flatten Array
URL: https://exercism.org/tracks/python/exercises/flatten-array



Instructions

Take a nested list and return a single flattened list with all values except nil/null.

The challenge is to write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure without any nil/null values.

For example:

input: [1,[2,3,null,4],[null],5]

output: [1,2,3,4,5]
'''
import itertools


def flatten(iterable: list) -> list:
    
    flatten_list = []
    for i in iterable:
        
        if type(i) == type([]):
            flatten_list.extend(flatten(i))
        
        else:
            if i != None and i != ():
                flatten_list.append(i)
    
    return flatten_list




# Test 1
display_task_name("I", "FlattenArray > empty")
display_example(
    'flatten([])', '[]'
)
print(flatten([]), "\n")



# Test 2
display_task_name("II", "FlattenArray > no nesting")
display_example(
    'flatten([0, 1, 2])',
    '[0, 1, 2]'
)

print(flatten([0, 1, 2]), "\n")



# Test 3
display_task_name("III", "FlattenArray > flattens a nested array")
display_example(
    'flatten([[[]]])',
    '[]'
)
print(flatten([[[]]]), "\n")