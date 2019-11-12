from dictionary import DictionaryNode
from grid import Grid
from knight_solver import KnightSolver


def test_simple_example():
    g = Grid.from_file('test_fixtures/grid1.txt')
    root = DictionaryNode(('algol', 'fortran', 'simula'))
    solver = KnightSolver(g, root)

    assert solver.find_longest_words() == ['fortran']


def test_example_with_multiple_solutions():
    g = Grid.from_file('test_fixtures/grid1.txt')
    root = DictionaryNode(('algol', 'fortran', 'fortraw', 'simula', 'sortran'))
    solver = KnightSolver(g, root)

    expected = ['fortraw', 'fortraw', 'fortran', 'sortran']
    assert solver.find_longest_words() == expected


def test_complex_dictionary():
    g = Grid.from_file('test_fixtures/grid2.txt')
    root = DictionaryNode.from_file('test_fixtures/loves_labour_lost.txt')
    solver = KnightSolver(g, root)

    assert solver.find_longest_words() == ['honorificabilitudinitatibus']
