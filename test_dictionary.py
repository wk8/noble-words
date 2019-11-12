from dictionary import DictionaryNode

_WORDS = 'aaa a ab abc ad bd z'.split(' ')


def test_dictionary_node():
    root = DictionaryNode(_WORDS)

    assert set(root.keys()) == set('abz')
    assert not root.is_word

    assert 'a' in root
    a = root['a']
    assert a.is_word
    assert 'a' in a
    assert not a['a'].is_word

    for word in _WORDS:
        current = root
        for letter in word:
            current = current[letter]
        assert current.is_word


def test_dictionary_from_basic_file():
    from_file = DictionaryNode.from_file('test_fixtures/simple_dict.txt')
    assert DictionaryNode(_WORDS) == from_file


def test_case_insensitive():
    with_case = 'aAa A ab abC ad bD z'.split(' ')
    assert DictionaryNode(_WORDS) == DictionaryNode(with_case)
