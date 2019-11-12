import string


class Grid(object):
    def __init__(self, *rows):
        if rows:
            self._width = len(rows[0])
            for row in rows:
                if len(row) != self._width:
                    raise RuntimeError('should be a rectangular matrix')
        else:
            self._width = 0
        self._rows = rows

        for i, row in enumerate(self._rows):
            for j, value in enumerate(row):
                if not self.__class__._is_single_character(value):
                    msg = 'grid values should be single characters, '
                    msg += 'got % instead at (%s, %s)' % (value, i, j)
                    raise RuntimeError(msg)
                row[j] = value.lower()

    @staticmethod
    def _is_single_character(s):
        if not isinstance(s, str) and len(s) == 1:
            return False
        return s[0] in string.ascii_letters

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return len(self._rows)

    # assumes i and j are valid coordinates
    def get(self, i, j):
        return self._rows[i][j]

    # returns an iterator for all valid knight moves from i, j
    # assumes i and j are valid coordinates
    def knight_moves(self, i, j):
        for dx, dy in ((1, 2), (2, 1)):
            for multiplier_dx in (-1, 1):
                x = i + dx * multiplier_dx
                if x < 0 or x >= self.height:
                    continue

                for multiplier_dy in (-1, 1):
                    y = j + dy * multiplier_dy

                    if y >= 0 and y < self.width:
                        yield x, y

    @classmethod
    def from_file(cls, file_path, delimiter=' '):
        with open(file_path) as input_file:
            lines = filter(bool, [line.strip() for line in input_file])
            return cls(*[line.split(delimiter) for line in lines])
