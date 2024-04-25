from itertools import groupby

def pack_consecutive_duplicates(list1):
    packed_duplicates = []
    
    for key, group in groupby(list1):
        group_list = list(group)
        
        if len(group_list) > 1:
            packed_duplicates.append(group_list)
        
    return packed_duplicates

def check(candidate):
    assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    assert pack_consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
    assert pack_consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==[['a', 'a'], ['b'], ['c'], ['d', 'd']]

check(pack_consecutive_duplicates)