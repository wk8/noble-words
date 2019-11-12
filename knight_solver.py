class KnightSolver(object):
    def __init__(self, grid, dictionary_root):
        self._grid = grid
        self._root = dictionary_root

    def find_longest_words(self):
        '''
        Returns a list of the longest words from the dictionary found
        in the grid; i.e. all words in the returned list have the same
        length.
        '''
        current_words = []
        current_lengths = 0

        for i in range(self._grid.height):
            for j in range(self._grid.width):
                current_words, current_lengths = self._find_longest_words_rec(
                    i, j, self._root, '', current_words, current_lengths)

        return current_words

    # returns the list of the longest words starting from i, j
    def _find_longest_words_rec(self, i, j, node, word, words, lengths):
        letter = self._grid.get(i, j)
        new_node = node.get(letter)
        if new_node is None:
            return words, lengths

        new_word = word + letter
        if new_node.is_word and len(new_word) >= lengths:
            if len(new_word) == lengths:
                words.append(new_word)
            else:
                words = [new_word]
                lengths = len(new_word)

        for new_i, new_j in self._grid.knight_moves(i, j):
            words, lengths = self._find_longest_words_rec(new_i, new_j,
                                                          new_node, new_word,
                                                          words, lengths)

        return words, lengths
