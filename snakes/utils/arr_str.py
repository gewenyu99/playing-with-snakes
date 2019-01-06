def elem_count(*args):
    """
    Takes in iterable arguments and returns a count of different elements
    :param args: iteralble
    :return: dict
    """
    count = {}
    for iterable in args:
        for elem in iterable:
            if elem not in count:
                count[elem] = 0
            count[elem] += 1
    return count

