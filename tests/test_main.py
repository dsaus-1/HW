from pytest_project.main import get_val


def test_get_val():
    '''
    ключ находится в словаре
    '''
    assert get_val({"hello": "world"}, "hello") == 'world'
    assert get_val({"hello": "world"}, "hello", "Not found") == 'world'


def test_get_val_not_found():
    '''
    ключа нет в словаре
    '''
    assert get_val({"hello": "world" }, "hell") == None
    assert get_val({"hello": "world"}, "hell", "Not found") == 'Not found'

def test_get_val_empty():
     '''
     пустой список
     '''
     assert get_val({}, "hello", "python") == 'python'
     assert get_val({}, "hello") == None
