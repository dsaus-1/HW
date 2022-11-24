

def get_val(collection, key, default=None):

    '''
    Функция возвращает значение из словаря по переданному ключу, если он существует. В ином случае возвращается default
    '''

    if key in collection:
        return collection[key]
    else:
        return default
