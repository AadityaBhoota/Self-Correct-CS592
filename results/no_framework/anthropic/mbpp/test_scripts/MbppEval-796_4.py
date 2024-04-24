def return_sum(dict):
    """
    Write function to find the sum of all items in the given dictionary.

    Examples:
    return_sum({'a': 100, 'b':200, 'c':300}) == 600
    return_sum({'a': 25, 'b':18, 'c':45}) == 88
    return_sum({'a': 36, 'b':39, 'c':49}) == 124
    """
    total = 0
    for value in dict.values():
        total += value
    return total

def check(candidate):
    assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
    assert return_sum({'a': 25, 'b':18, 'c':45}) == 88
    assert return_sum({'a': 36, 'b':39, 'c':49}) == 124

check(return_sum)