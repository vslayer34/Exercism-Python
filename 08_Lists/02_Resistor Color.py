from helper import display_task_name, display_example

'''
Problem: https://exercism.org/tracks/python/exercises/resistor-color
'''

colors_encodes =[
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]

def color_code(color: str) -> int:
    return colors_encodes.index(color)


def colors():
    return colors_encodes




# Test 1
display_task_name("I", "ResistorColor > black")
display_example(
    'color_code("black")',
    '0'
)
print(color_code("black"))



# Test 2
display_task_name("II", "ResistorColor > white")
display_example(
    'color_code("white")',
    '9'
)
print(color_code("white"))



# Test 3
display_task_name("III", "ResistorColor > orange")
display_example(
    'color_code("orange")',
    '3'
)
print(color_code("orange"))



# Test 4
display_task_name("IV", "ResistorColor > colors")
display_example(
    "colors()",
    '["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]'
)
print(colors())