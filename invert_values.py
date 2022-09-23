# Invert values
# Given a set of numbers, return the additive inverse of each.
# Each positive becomes negatives, and the negatives become positives.
# You can assume that all values are integers. Do not mutate the input array/list.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []

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
