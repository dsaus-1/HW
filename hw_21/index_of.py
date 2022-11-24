


def index_of(coll, value, from_index=0):
    '''
     возвращает первый индекс, по которому переданное значение может быть найдено в списке или -1, если такого значения нет.
    '''
    length = len(coll)

    if length == 0:
         return -1

    index = from_index

    if index < 0:
        if index < -length:
            index = 0
        else:
            index += length

    try:
        return coll.index(value, index)
    except ValueError:
        return -1
