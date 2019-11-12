from utils import letter_substrings


def test_letter_substrings():
    s = '   Truly, Master Holofernes, the epithets are sweetly\n'
    expected = ['Truly', 'Master', 'Holofernes', 'the',
                'epithets', 'are', 'sweetly']
    assert list(letter_substrings(s)) == expected
