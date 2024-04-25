def intersection_array(array_nums1,array_nums2):
    '''
    Write a function to find the intersection of two arrays.

    Examples:
    intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]) == [1, 2, 8, 9]
    intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9]) == [3,5,7,9]
    intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40]) == [10]
    '''
    return sorted(list(intersection_set))

def check(candidate):
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]

check(intersection_array)