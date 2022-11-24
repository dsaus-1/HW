

def get(coll, index, default=None):
    '''
     извлекает из списка значение по указанному индексу, если индекс существует. Если индекс не существует, возвращает значение по умолчанию. Функция работает только с неотрицательными индексами
    '''
    if index >= len(coll) or index < 0:
        if default is not None:
            return default
        return None

    return coll[index] 
