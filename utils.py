import re


_LETTER_REGEXES = re.compile('[a-zA-Z]+')


def letter_substrings(s):
    '''
    Returns an iterator for all substrings of s comprised only of
    a-z A-Z letters
    '''
    for match in _LETTER_REGEXES.finditer(s):
        yield match.group(0)
