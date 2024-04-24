def flatten_list(list1):
    """
    Write a function to flatten a given nested list structure.

    Examples:
    flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    flatten_list([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]) == [10, 20, 40, 30, 56, 25, 10, 20, 33, 40]
    flatten_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]) == [1, 2, 3, 4, 5, 6, 10, 11, 12, 7, 8, 9]
    """
    result = []

    def _flatten(lst):
        for item in lst:
            if isinstance(item, list):
                _flatten(item)
            else:
                result.append(item)

    _flatten(list1)
    return result

def check(candidate):
    assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    assert flatten_list([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])==[10, 20, 40, 30, 56, 25, 10, 20, 33, 40]
    assert flatten_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[1, 2, 3, 4, 5, 6, 10, 11, 12, 7, 8, 9]

check(flatten_list)