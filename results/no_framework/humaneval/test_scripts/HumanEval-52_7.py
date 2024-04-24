def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t."""
    return all(num < t for num in l)

# Testing the function with sample inputs





METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10], 100)
    assert not candidate([1, 20, 4, 10], 5)
    assert candidate([1, 20, 4, 10], 21)
    assert candidate([1, 20, 4, 10], 22)
    assert candidate([1, 8, 4, 10], 11)
    assert not candidate([1, 8, 4, 10], 10)


check(below_threshold)