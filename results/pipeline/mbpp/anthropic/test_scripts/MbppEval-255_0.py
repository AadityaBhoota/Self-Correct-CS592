from itertools import combinations_with_replacement

def combinations_colors(l, n):
    """
    Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list of lists.

    Examples:
    combinations_colors( ["Red","Green","Blue"],1) == [['Red'], ['Green'], ['Blue']]
    combinations_colors( ["Red","Green","Blue"],2) == [['Red', 'Red'], ['Red', 'Green'], ['Red', 'Blue'], ['Green', 'Green'], ['Green', 'Blue'], ['Blue', 'Blue']]
    combinations_colors( ["Red","Green","Blue"],3) == [['Red', 'Red', 'Red'], ['Red', 'Red', 'Green'], ['Red', 'Red', 'Blue'], ['Red', 'Green', 'Green'], ['Red', 'Green', 'Blue'], ['Red', 'Blue', 'Blue'], ['Green', 'Green', 'Green'], ['Green', 'Green', 'Blue'], ['Green', 'Blue', 'Blue'], ['Blue', 'Blue', 'Blue']]
    """
    return [list(combo) for combo in combinations_with_replacement(l, n)]

def check(candidate):
    assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
    assert combinations_colors( ["Red","Green","Blue"],2)==[('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Blue')]
    assert combinations_colors( ["Red","Green","Blue"],3)==[('Red', 'Red', 'Red'), ('Red', 'Red', 'Green'), ('Red', 'Red', 'Blue'), ('Red', 'Green', 'Green'), ('Red', 'Green', 'Blue'), ('Red', 'Blue', 'Blue'), ('Green', 'Green', 'Green'), ('Green', 'Green', 'Blue'), ('Green', 'Blue', 'Blue'), ('Blue', 'Blue', 'Blue')]

check(combinations_colors)