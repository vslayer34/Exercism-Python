'''
Exercise: Hamming
URL: https://exercism.org/tracks/python/exercises/hamming
Instructions

Calculate the Hamming Distance between two DNA strands.

Your body is made up of cells that contain DNA. Those cells regularly wear out and need replacing, which they achieve by dividing into daughter cells. In fact, the average human body experiences about 10 quadrillion cell divisions in a lifetime!

When cells divide, their DNA replicates too. Sometimes during this process mistakes happen and single pieces of DNA get encoded with the incorrect information. If we compare two strands of DNA and count the differences between them we can see how many mistakes occurred. This is known as the "Hamming Distance".

We read DNA using the letters C,A,G and T. Two strands might look like this:

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^

They have 7 differences, and therefore the Hamming Distance is 7.

The Hamming Distance is useful for lots of things in science, not just biology, so it's a nice phrase to be familiar with :)
Implementation notes

The Hamming distance is only defined for sequences of equal length, so an attempt to calculate it between sequences of different lengths should not work.
Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should always include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the built in error types, but should still include a meaningful message.

This particular exercise requires that you use the raise statement to "throw" a ValueError when the strands being checked are not the same length. The tests will only pass if you both raise the exception and include a message with it.

To raise a ValueError with a message, write the message as an argument to the exception type:

# When the sequences being passed are not the same length.
raise ValueError("Strands must be of equal length.")

'''
from helper import display_task_name, display_example


def distance(strand_a: str, strand_b: str) -> int:

    number_of_differences = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    else:
        for i in range(0, len(strand_a)):
            if strand_a[i] != strand_b[i]:
                number_of_differences += 1
    
    return number_of_differences




# Test 1
display_task_name("I", "Hamming > empty strands")
display_example(
    'distance("", "")',
    0
)
print(distance("", ""), "\n")




# Test 2
display_task_name("II", "Hamming > single letter identical strands")
display_example(
    'distance("A", "A")',
    0
)
print(distance("A", "A"), "\n")




# Test 3
display_task_name("III", "Hamming > single letter different strands")
display_example(
    'distance("G", "T")',
    1
)
print(distance("G", "T"), "\n")




# Test 4
display_task_name("IV", "Hamming > long identical strands")
display_example(
    'distance("GGACTGAAATCTG", "GGACTGAAATCTG")',
    0
)
print(distance("GGACTGAAATCTG", "GGACTGAAATCTG"), "\n")




# Test 5
display_task_name("V", "Hamming > long different strands")
display_example(
    'distance("GGACGGATTCTG", "AGGACGGATTCT")',
    9
)
print(distance("GGACGGATTCTG", "AGGACGGATTCT"), "\n")




# Test 6
display_task_name("VI", "Hamming > disallow first strand longer")
display_example(
    'distance("AATG", "AAA")',
    'Strands must be of equal length.'
)
print(distance("AATG", "AAA"), "\n")




# Test 7
display_task_name("VII", "Hamming > disallow second strand longer")
display_example(
    'distance("ATA", "AGTG")',
    'Strands must be of equal length.'
)
print(distance("ATA", "AGTG"), "\n")




# Test 8
display_task_name("VIII", "Hamming > disallow empty first strand")
display_example(
    'distance("", "G")',
    'Strands must be of equal length.'
)
print(distance("", "G"), "\n")




# Test 9
display_task_name("IX", "Hamming > disallow empty second strand")
display_example(
    'distance("G", "")',
    'Strands must be of equal length.'
)
print(distance("G", ""), "\n")