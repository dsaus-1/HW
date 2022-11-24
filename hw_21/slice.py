

def my_slice(coll, start=0, end=None):
    '''
    возвращает новый список, содержащий копию части исходного списка
    '''
    length = len(coll)

    normalized_end = length if end is None else end

    if length == 0:
        return []

    normalized_start = start

    if normalized_start < 0:
        if normalized_start < -length:
            normalized_start = 0
        else:
            normalized_start += length

    return coll[normalized_start:normalized_end]
