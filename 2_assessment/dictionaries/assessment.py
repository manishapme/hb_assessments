"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    wordlist = {}
    # iterate through phrase, setting each word as a key
    # incrementing the value of the word each time to get count
    for word in phrase.split(" "):
        wordlist[word] = wordlist.get(word, 0) + 1

    return wordlist


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """

    # store info in a dictionary
    melons = { 
        "Watermelon": 2.95,
        "Cantaloupe": 2.50,
        "Musk": 3.25,
        "Christmas": 14.25, 
    }

    return melons.get(melon_name, "No price found")


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    
    words_by_length = {}
    for word in words:
        # create a dictionary where the length of word is the key
        key = len(word)
        # and value is the list of words of that length
        words_by_length[key] = words_by_length.get(key, [])
        words_by_length[key].append(word)
        # sort list of words
        words_by_length[key] = sorted(words_by_length[key])

    # [ words_by_length.get(len(word), []).append(word) for word in words ]

    result = []
    # sort the keys in the dictionary and loop through 
    for key in sorted(words_by_length.keys()):
        # append a tuple to the result list for each key
        result.append((key, words_by_length[key]))


    return result


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    #normalize data into a dictionary
    pirate_dictionary = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "man": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be",
    }

    newphrase = []

    for word in phrase.split():
        # substitute pirate words as needed
        if word in pirate_dictionary:
            word = pirate_dictionary[word]

        newphrase.append(word)
    # convert newphrase back to string at end
    return " ".join(newphrase)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    #we know the first word in result is always the first name passed
    result = [names[0]]

    # create a dictionary using the first letter of each word as a key
    names_by_first_letter = {}

    # exclude the first name
    for name in names[1:]:
        names_by_first_letter[name[0]] = names_by_first_letter.get(name[0], [])
        #note that the names are appended to the list in the order they appear
        names_by_first_letter[name[0]].append(name)

    # play game
    i = 0
    # we can never has a result longer than the list passed
    while i < len(names):
        try:
            # Use the last letter of that word to look for the next word.
            last_letter = result[-1][-1]
            # find the *first* word starting with that letter
            next_word = names_by_first_letter[last_letter][0]

            #ensure the word hasn't been used before
            if next_word not in result:
                 result.append(next_word)
                 # after appending it to result, remove from dictionary
                 # ensuring another word will get chosen next time
                 del names_by_first_letter[last_letter][0]
        except IndexError:
            pass
        i += 1


    return result

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
