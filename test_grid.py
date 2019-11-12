from grid import Grid


def test_simple_grid():
    g = Grid.from_file('test_fixtures/grid1.txt')

    assert g.width == 8
    assert g.height == 8

    assert g.get(0, 0) == 'q'
    assert g.get(0, 1) == 'w'
    assert g.get(1, 0) == 'o'
    assert g.get(6, 3) == 'm'

    assert list(g.knight_moves(0, 0)) == [(1, 2), (2, 1)]
    assert list(g.knight_moves(7, 6)) == [(6, 4), (5, 5), (5, 7)]
    assert list(g.knight_moves(3, 4)) == [(2, 2), (2, 6), (4, 2), (4, 6),
                                          (1, 3), (1, 5), (5, 3), (5, 5)]


def test_empty_grid():
    g = Grid()

    assert g.width == 0
    assert g.height == 0


def test_small_grid():
    g = Grid(['A', 'B'], ['C', 'D'])

    assert g.width == 2
    assert g.height == 2

    assert list(g.knight_moves(0, 0)) == []
