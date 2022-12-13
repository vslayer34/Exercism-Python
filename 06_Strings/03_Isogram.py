'''
Exercise: Isogram
URL: https://exercism.org/tracks/python/exercises/isogram

Instructions

Determine if a word or phrase is an isogram.

An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

    lumberjacks
    background
    downstream
    six-year-old

The word isograms, however, is not an isogram, because the s repeats.
'''

from helper import display_task_name, display_example

def is_isogram(string: str) -> bool:
    *list_of_letters, = string.lower()
    
    for letter in list_of_letters:

        # Skip '-' or the space between the words
        if letter == "-" or letter == " ":
            continue
        
        elif list_of_letters.count(letter) > 1:
            return False
    
    return True








# Test 1
display_task_name("I", "Isogram > empty string")
display_example(
    'is_isogram("")',
    'True'
)
print(is_isogram(""), "\n")



# Test 2
display_task_name("II", "Isogram > isogram with only lower case characters")
display_example(
    'is_isogram("isogram")',
    'True'
)
print(is_isogram("isogram"), "\n")



# Test 3
display_task_name("III", "Isogram > word with one duplicated character")
display_example(
    'is_isogram("eleven")',
    'False'
)
print(is_isogram("eleven"), "\n")



# Test 4
display_task_name("IV", "Isogram > word with one duplicated character from the end of the alphabet")
display_example(
    'is_isogram("zzyzx")',
    'False'
)
print(is_isogram("zzyzx"), "\n")



# Test 5
display_task_name("V", "Isogram > longest reported english isogram")
display_example(
    'is_isogram("subdermatoglyphic")',
    'True'
)
print(is_isogram("subdermatoglyphic"), "\n")



# Test 6
display_task_name("VI", "Isogram > word with duplicated character in mixed case")
display_example(
    'is_isogram("Alphabet")',
    'False'
)
print(is_isogram("Alphabet"), "\n")



# Test 7
display_task_name("VII", "Isogram > word with duplicated character in mixed case lowercase first")
display_example(
    'is_isogram("alphAbet")',
    'False'
)
print(is_isogram("alphAbet"), "\n")



# Test 8
display_task_name("VIII", "Isogram > hypothetical isogrammic word with hyphen")
display_example(
    'is_isogram("thumbscrew-japingly")',
    'True'
)
print(is_isogram("thumbscrew-japingly"), "\n")



# Test 9
display_task_name("IX", "Isogram > hypothetical word with duplicated character following hyphen")
display_example(
    'is_isogram("thumbscrew-jappingly")',
    'False'
)
print(is_isogram("thumbscrew-jappingly"), "\n")



# Test 10
display_task_name("X", "Isogram > isogram with duplicated hyphen")
display_example(
    'is_isogram("six-year-old")',
    'True'
)
print(is_isogram("six-year-old"), "\n")



# Test 11
display_task_name("XI", "Isogram > made up name that is an isogram")
display_example(
    'is_isogram("Emily Jung Schwartzkopf")',
    'True'
)
print(is_isogram("Emily Jung Schwartzkopf"), "\n")



# Test 12
display_task_name("XII", "Isogram > duplicated character in the middle")
display_example(
    'is_isogram("accentor")',
    'False'
)
print(is_isogram("accentor"), "\n")



# Test 13
display_task_name("XIII", "Isogram > same first and last characters")
display_example(
    'is_isogram("angola")',
    'False'
)
print(is_isogram("angola"), "\n")



# Test 14
display_task_name("XIV", "Isogram > word with duplicated character and with two hyphens")
display_example(
    'is_isogram("up-to-date")',
    'False'
)
print(is_isogram("up-to-date"), "\n")