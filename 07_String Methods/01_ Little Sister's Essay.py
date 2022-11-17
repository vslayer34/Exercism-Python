"""
Functions to help edit essay homework using string manipulation.
https://exercism.org/tracks/python/exercises/little-sisters-essay
"""


def capitalize_title(title: str):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
    return title.title()


def check_sentence_ending(sentence: str):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    return sentence.endswith(".")


def clean_up_spacing(sentence: str):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """
    return sentence.replace(old_word, new_word)



# Task I : Capitalize the title of the paper
# >>> capitalize_title("my hobbies")
# "My Hobbies"
print(capitalize_title("my hobbies"))



# Task II: Check if each sentence ends with a period
# >>> check_sentence_ending("I like to hike, bake, and read.")
# True
print(check_sentence_ending("I like to hike, bake, and read."))



# Task III: Clean up spacing
# >>> clean_up_spacing(" I like to go on hikes with my dog.  ")
# "I like to go on hikes with my dog."
print(clean_up_spacing(" I like to go on hikes with my dog.  "))



# Task IV: Replace words with a synonym
# >>> replace_word_choice("I bake good cakes.", "good", "amazing")
# "I bake amazing cakes."
print(replace_word_choice("I bake good cakes.", "good", "amazing"))