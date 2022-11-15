"""
Functions for creating, transforming, and adding prefixes to strings.
https://exercism.org/tracks/python/exercises/little-sisters-vocab
"""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    # new list for words
    newList = []
    prefix = vocab_words[0]
    for i in range(len(vocab_words)):
        if vocab_words[i] is prefix:
            newList.append(vocab_words[i])
        else:
            newList.append(prefix + vocab_words[i])
    
    return " :: ".join(newList)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    original_word = word.removesuffix("ness")
    if original_word[-1] is not "i":
        return original_word
    else:
        removed_i = original_word[0:-1]
        return removed_i + "y"


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """
    targeted_word = sentence.split()[index]
    if targeted_word.endswith("."):
        modified_word = targeted_word.replace(".", "en")
    else:
        modified_word = targeted_word + "en"
    return modified_word




# Task I: Add a prefix to a word
# >>> add_prefix_un("happy")
# 'unhappy'
print(add_prefix_un("happy"), "\n")

# >>> add_prefix_un("manageable")
# 'unmanageable'
print(add_prefix_un("manageable"), "\n")



# Task II: Add prefixes to word groups
# >>> make_word_groups(['en', 'close', 'joy', 'lighten'])
# 'en :: enclose :: enjoy :: enlighten'
print(make_word_groups(['en', 'close', 'joy', 'lighten']), "\n")

# >>> make_word_groups(['pre', 'serve', 'dispose', 'position'])
# 'pre :: preserve :: predispose :: preposition'
print(make_word_groups(['pre', 'serve', 'dispose', 'position']), "\n")

# >> make_word_groups(['auto', 'didactic', 'graph', 'mate'])
# 'auto :: autodidactic :: autograph :: automate'
print(make_word_groups(['auto', 'didactic', 'graph', 'mate']), "\n")

# >>> make_word_groups(['inter', 'twine', 'connected', 'dependent'])
# 'inter :: intertwine :: interconnected :: interdependent'
print(make_word_groups(['inter', 'twine', 'connected', 'dependent']), "\n")



# Task III: Remove a suffix from a word
# >>> remove_suffix_ness("heaviness")
# 'heavy'
print(remove_suffix_ness("heaviness"), "\n")

# >>> remove_suffix_ness("sadness")
# 'sad'
print(remove_suffix_ness("sadness"), "\n")



# Task IV: Extract and transform a word
# >>> adjective_to_verb('I need to make that bright.', -1 )
# 'brighten'
print(adjective_to_verb('I need to make that bright.', -1 ), "\n")

# >>> adjective_to_verb('It got dark as the sun set.', 2)
# 'darken'
print(adjective_to_verb('It got dark as the sun set.', 2), "\n")