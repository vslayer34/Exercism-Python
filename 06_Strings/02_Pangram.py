from helper import display_task_name, display_example

'''
Excersise: Pangram
URL: https://exercism.org/tracks/python/exercises/pangram
Instructions

Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, "every letter") is a sentence using every letter of the alphabet at least once. The best known English pangram is:

    The quick brown fox jumps over the lazy dog.

The alphabet used consists of letters a to z, inclusive, and is case insensitive.
'''

def is_pangram(sentence: str) -> bool:
    alphabets = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    lower_sentence = sentence.lower()
    
    for character in alphabets:
        
        if character.lower() not in lower_sentence:
            return False
    
    return True




# Test 1
display_task_name("I", "Pangram > empty sentence")
display_example(
    'is_pangram("")',
    'False'
)
print(is_pangram(""), "\n")




# Test 2
display_task_name("II", "Pangram > perfect lower case")
display_example(
    'is_pangram("abcdefghijklmnopqrstuvwxyz")',
    'True'
)
print(is_pangram("abcdefghijklmnopqrstuvwxyz"), "\n")




# Test 3
display_task_name("III", "Pangram > only lower case")
display_example(
    'is_pangram("the quick brown fox jumps over the lazy dog")',
    'True'
)
print(is_pangram("the quick brown fox jumps over the lazy dog"), "\n")




# Test 4
display_task_name("IV", "Pangram > missing the letter x")
display_example(
    'is_pangram("a quick movement of the enemy will jeopardize five gunboats")',
    'False'
)
print(is_pangram("a quick movement of the enemy will jeopardize five gunboats"), "\n")




# Test 5
display_task_name("V", "Pangram > missing the letter h")
display_example(
    'is_pangram("five boxing wizards jump quickly at it")',
    'False'
)
print(is_pangram("five boxing wizards jump quickly at it"), "\n")




# Test 6
display_task_name("VI", "Pangram > with underscores")
display_example(
    'is_pangram("the quick brown fox jumps over the lazy dog")',
    'True'
)
print(is_pangram("the quick brown fox jumps over the lazy dog"), "\n")




# Test 7
display_task_name("VII", "Pangram > with numbers")
display_example(
    'is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs")',
    'True'
)
print(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), "\n")




# Test 8
display_task_name("VIII", "Pangram > missing letters replaced by numbers")
display_example(
    'is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog")',
    'False'
)
print(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), "\n")




# Test 9
display_task_name("IX", "Pangram > mixed case and punctuation")
display_example(
    'is_pangram(\'"Five quacking Zephyrs jolt my wax bed."\')',
    'True'
)
print(is_pangram('"Five quacking Zephyrs jolt my wax bed."'), "\n")




# Test 10
display_task_name("X", "Pangram > a m and a m are 26 different characters but not a pangram")
display_example(
    'is_pangram("abcdefghijklm ABCDEFGHIJKLM")',
    'False'
)
print(is_pangram("abcdefghijklm ABCDEFGHIJKLM"), "\n")




# Test 11
display_task_name("XI", "Pangram > sentence without lower bound")
display_example(
    'is_pangram("bcdefghijklmnopqrstuvwxyz")',
    'False'
)
print(is_pangram("bcdefghijklmnopqrstuvwxyz"), "\n")




# Test 12
display_task_name("XII", "Pangram > sentence without upper bound")
display_example(
    'is_pangram("abcdefghijklmnopqrstuvwxy")',
    'False'
)
print(is_pangram("abcdefghijklmnopqrstuvwxy"), "\n")