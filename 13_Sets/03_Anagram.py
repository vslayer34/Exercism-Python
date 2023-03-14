from helper import display_task_name, display_example

'''
Exersice Name: Anagram
URL: https://exercism.org/tracks/python/exercises/anagram

Instructions

An anagram is a rearrangement of letters to form a new word: for example "owns" is an anagram of "snow". A word is not its own anagram: for example, "stop" is not an anagram of "stop".

Given a target word and a set of candidate words, this exercise requests the anagram set: the subset of the candidates that are anagrams of the target.

The target and candidates are words of one or more ASCII alphabetic characters (A-Z and a-z). Lowercase and uppercase characters are equivalent: for example, "PoTS" is an anagram of "sTOp", but StoP is not an anagram of sTOp. The anagram set is the subset of the candidate set that are anagrams of the target (in any order). Words in the anagram set should have the same letter case as in the candidate set.

Given the target "stone" and candidates "stone", "tones", "banana", "tons", "notes", "Seton", the anagram set is "tones", "notes", "Seton".
'''


def find_anagrams(word: str, candidates: list) -> list:
    empty_list = []
    
    # # create a set of the world
    # word_set = {letter.lower() for letter in word}

    # # create a list consistent of sets of the words in it
    # list_of_candidates_letter = [{*word.lower()} for word in candidates]
    
    # list_of_equal_sets = [ word_set == set for set in list_of_candidates_letter]

    # for i in range(0, len(list_of_equal_sets)):
    #     if list_of_equal_sets[i] == True:
    #         empty_list.append(candidates[i])
    
    # return empty_list
    for candidate in candidates:
        if candidate.casefold() != word.casefold() and sorted(candidate.casefold()) == sorted(word.casefold()):
            empty_list.append(candidate)
        
    return empty_list





# # Test 1
# display_task_name('I', 'Anagram > no matches')
# display_example(
#     'find_anagrams("diaper", ["hello", "world", "zombies", "pants"])',
#     '[]'
# )
# print(find_anagrams("diaper", ["hello", "world", "zombies", "pants"]), "\n")



# # Test 2
# display_task_name("II", "Anagram > detects two anagrams")
# display_example(
#     'find_anagrams("solemn", ["lemons", "cherry", "melons"])',
#     '["lemons", "melons"]'
# )
# print(find_anagrams("solemn", ["lemons", "cherry", "melons"]), "\n")



# Test 3
display_task_name("III", "does not detect anagram subsets")
display_example(
    'find_anagrams("good", ["dog", "goody"])',
    '[]'
)
print(find_anagrams("good", ["dog", "goody"]), "\n")


# Test2
display_task_name("II", "Anagram > detects two anagrams")
display_example(
    'find_anagrams("solemn", ["lemons", "cherry", "melons"])',
    ["lemons", "melons"]
)
print(find_anagrams("solemn", ["lemons", "cherry", "melons"]), "\n")