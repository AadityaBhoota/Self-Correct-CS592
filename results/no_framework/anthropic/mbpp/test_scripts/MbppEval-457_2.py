def Find_Min(lst):
    """
    Write a python function to find the sublist having minimum length.

    Examples:
    Find_Min([[1],[1,2],[1,2,3]]) == [1]
    Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']
    """
    if not lst:
        return []

    min_length = float('inf')
    min_sublist = None

    for sublst in lst:
        if len(sublst) < min_length:
            min_length = len(sublst)
            min_sublist = sublst

    return min_sublist

def check(candidate):
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
    assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']

check(Find_Min)