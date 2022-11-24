


def set_(coll, path, value):
    new_coll = coll
    for i in path[:-1]:
        if i in new_coll:
            new_coll = new_coll[i]
        else:
            new_coll[i] = {}
            new_coll = new_coll[i]
    new_coll[path[-1]] = value
    return coll
