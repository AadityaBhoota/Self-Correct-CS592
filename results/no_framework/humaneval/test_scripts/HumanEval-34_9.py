def unique(l: list):
    return sorted(list(set(l)))

# Test the function with the example provided in the docstring




METADATA = {}


def check(candidate):
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]


check(unique)