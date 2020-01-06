def text_to_list(text):
    """
    Takes a body of text and returns a list of each word in lowercase
    """
    for char in ',\[]<>()/;":?_*!\n':
        text = text.replace(char, ' ')
    text = text.lower()
    text = text.split()
    result = []
    for i in range(len(text)):
        if text[i] != '-' and text[i] != '--':
            result.append(text[i])
    return result


def gender_word_list(list1, list2):
    """
    Takes two lists of words (strings) and checks how many times the words in list 2 are in list1.
    Returns a list with each word appearing in both lists.
    """
    result = []
    for word1 in list1:
        for word2 in list2:
            if word1.startswith(word2):
                word1 = word1.replace('.', '')
                result.append(word1)
            elif word1 == word2:
                result.append(word1)
    return result


def gender_exact_word_list(list1, list2):
    """
    Takes two lists of words (strings) and checks how many times the exact words in list 2 are in list1.
    Returns a list with each word appearing on both lists.
    """
    result = []
    for word1 in list1:
        for word2 in list2:
            if word1 == word2:
                result.append(word1)
    return result


def list_of_words_to_dict(wordlist):
    """
    Takes a list of words (strings) and converts them to a dictionary.
    Keys are the words from the list, values are the number of instances of the word in the list.
    """
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    return worddict


def list_of_gender_words(wordlist):
    """
    Takes a list of words(strings) and converts them to a list with each word represented once.
    """
    worddict = list_of_words_to_dict(wordlist)
    gender_list = list(worddict.keys())
    return gender_list


def phrase_in_text(text, genderlist):
    """
    Finds items from a list of phrases in a body of textself.
    Returns a dictionary with the phrases found and the number of instances found.
    """
    result = {}
    text = text.lower()
    for word in genderlist:
        if word in text:
            result[word] = text.count(word)
    return result


def dictcount(dict):
    count = 0
    for key in dict:
        words = key.split()
        items = len(words)
        count += (dict[key] * items)
    return count


def int_str(val, keyspace):
    """ Turn a positive integer into a string. """
    assert val >= 0
    out = ""
    while val > 0:
        val, digit = divmod(val, len(keyspace))
        out += keyspace[digit]
    return out[::-1]


def str_int(val, keyspace):
    """ Turn a string into a positive integer. """
    out = 0
    for c in val:
        out = out * len(keyspace) + keyspace.index(c)
    return out

keyspace = 'xpz3mw1ndj0r8ul9-hg7seot2qi6yf4ck_5abv'
