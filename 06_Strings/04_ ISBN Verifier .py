from helper import display_task_name, display_example

'''
Exersice:  ISBN Verifier
URL: https://exercism.org/tracks/python/exercises/isbn-verifier

Instructions

The ISBN-10 verification process is used to validate book identification numbers. These normally contain dashes and look like: 3-598-21508-8
ISBN

The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens, and can be checked for their validity by the following formula:

(d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0

If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.

----------------------------------------------------------------------------------------------------------------------------

Example

Let's take the ISBN-10 3-598-21508-8. We plug it in to the formula, and get:

(3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0

Since the result is 0, this proves that our ISBN is valid.

----------------------------------------------------------------------------------------------------------------------------

Task

Given a string the program should check if the provided string is a valid ISBN-10. Putting this into place requires some thinking about preprocessing/parsing of the string prior to calculating the check digit for the ISBN.

The program should be able to verify ISBN-10 both with and without separating dashes.

----------------------------------------------------------------------------------------------------------------------------

Caveats

Converting from strings to numbers can be tricky in certain languages.
Now, it's even trickier since the check digit of an ISBN-10 may be 'X' (representing '10'). 
For instance 3-598-21507-X is a valid ISBN-10.
'''

def check_formula(isbn: str) -> int:
    # sum ad descending counter
    sum: int = 0
    decsending_counter: int = 10

    # loop through the isbn and multiply the digit
    # with the desending order digits
    for i in range(0, len(isbn)):
        # check if last character is x and replace it with 10
        if (i == len(isbn) - 1) and isbn[i].casefold() == "x".casefold():
            sum += 10 * decsending_counter
            break
        sum += int(isbn[i]) * decsending_counter
        decsending_counter -= 1

    # return the sum
    return sum


def is_valid(isbn: str) -> bool:
    # first remove the dashes
    isbn_with_no_dashes = isbn.replace('-', '')

    # check the isbn length
    if (len(isbn_with_no_dashes) != 10):
        return False

    # try the formula
    # if faild return false
    try:
        formula_result = check_formula(isbn_with_no_dashes)
    except:
        return False
    
    # check the valid condition
    return formula_result % 11 == 0










# Test 1
display_task_name("I", "IsbnVerifier > valid isbn")
display_example(
    'is_valid("3-598-21508-8")',
    True
)
print(is_valid("3-598-21508-8"), '\n')


# Test 2
display_task_name("II", "IsbnVerifier > valid isbn with a check digit of 10")
display_example(
    'is_valid("3-598-21507-X")',
    True
)
print(is_valid("3-598-21507-X"), '\n')



# Test 4
display_task_name("IV", "IsbnVerifier > check digit is a character other than x")
display_example(
    'is_valid("3-598-21507-A")',
    False
)
print(is_valid("3-598-21507-A"), '\n')



# Test 12
display_task_name("XII", "IsbnVerifier > too short isbn")
display_example(
    'is_valid("00")',
    False
)
print(is_valid("00"), '\n')



# Test 8
display_task_name("VIII", "IsbnVerifier > valid isbn without separating dashes")
display_example(
    'is_valid("3598215088")',
    True
)
print(is_valid("3598215088"), '\n')