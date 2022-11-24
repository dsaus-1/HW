from hw_21.index_of import index_of

def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    assert index_of([2, 7, 3, 2, 4], 2, 2) == 3


def test_index_of_clean_list():
    assert index_of([], 2) == -1
    assert index_of([], 2, 5) == -1


def test_index_of_less_zero():
    assert index_of([2, 7, 3], 3, -2) == 2


def test_index_of_exceptions():
    assert index_of([2, 7, 3, 2, 4], 2, 6) == -1
