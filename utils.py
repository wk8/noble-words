import re


_LETTERS_REGEX = re.compile('[a-zA-Z]+')


def letter_substrings(s):
    '''
    Returns an iterator for all substrings of s comprised only of
    a-z A-Z letters
    '''
    for match in _LETTERS_REGEX.finditer(s):
        yield match.group(0)
