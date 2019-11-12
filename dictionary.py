from utils import letter_substrings


class DictionaryNode(dict):
    '''
    Represents a list of words as a tree, for fast lookups
    of potential suffixes to get to a valid word from a given
    prefix
    '''

    def __init__(self, words_iterator=()):
        super().__init__({})
        self._is_word = False

        for word in words_iterator:
            word = word.strip().lower()
            if word:
                self._add_word(word)

    @property
    def is_word(self):
        return self._is_word

    @classmethod
    def from_file(cls, file_path):
        with open(file_path) as input_file:
            def iterator():
                for line in input_file:
                    for substr in letter_substrings(line):
                        yield substr
            return cls(iterator())

    def _add_word(self, word):
        if not word:
            self._is_word = True
            return
        first_letter, rest = word[0], word[1:]
        child = self.get(first_letter, DictionaryNode())
        child._add_word(rest)
        self[first_letter] = child
