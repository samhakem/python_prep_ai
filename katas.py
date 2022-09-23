def invert(lst):
    """
    Step 1: given a set of numbers, iterate over each in the set
    Step 2: multiply each number by -1
    Step 3: return the new array
    :param lst: any given array
    :return: new additive inverse array
    """
    for n in lst:
        return [n * -1 for n in lst]
    return []
