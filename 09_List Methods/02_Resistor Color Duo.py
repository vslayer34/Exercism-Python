from helper import display_task_name, display_example


# List of band of colors
band_of_colors = [
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


def value(colors: list) -> int:
    first_value = str(band_of_colors.index(colors[0]))
    second_value = str(band_of_colors.index(colors[1]))
    resistor_value =  first_value + second_value
    return int(resistor_value)




# Test 1
display_task_name("I", "ResistorColorDuo > brown and black")
display_example(
    'value(["brown", "black"])',
    '10'
)
print(value(["brown", "black"]), "\n")



# Test 2
display_task_name("II", "ResistorColorDuo > blue and grey")
display_example(
    'value(["blue", "grey"])',
    '68'
)
print(value(["blue", "grey"]), "\n")



# Test 3
display_task_name("II", "ResistorColorDuo > yellow and violet")
display_example(
    'value(["yellow", "violet"])',
    '47'
)
print(value(["yellow", "violet"]), "\n")



# Test 4
display_task_name("IV", "ResistorColorDuo > white and red")
display_example(
    'value(["white", "red"])',
    '92'
)
print(value(["white", "red"]), "\n")



# Test 5
display_task_name("V", "ResistorColorDuo > orange and orange")
display_example(
    'value(["orange", "orange"])',
    '33'
)
print(value(["orange", "orange"]), "\n")



# Test 6
display_task_name("VI", "ResistorColorDuo > ignore additional colors")
display_example(
    'value(["green", "brown", "orange"])',
    '51'
)
print(value(["green", "brown", "orange"]), "\n")



# Test 7
display_task_name("VII", "ResistorColorDuo > black and brown one digit")
display_example(
    'value(["black", "brown"])',
    '1'
)
print(value(["black", "brown"]), "\n")