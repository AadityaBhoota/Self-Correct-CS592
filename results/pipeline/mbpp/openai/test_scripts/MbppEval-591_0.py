def swap_List(newList):
    if len(newList) > 1:
        new_list = newList.copy()
        new_list[0], new_list[-1] = new_list[-1], new_list[0]
        return new_list
    else:
        return newList

def check(candidate):
    assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
    assert swap_List([1, 2, 3]) == [3, 2, 1]
    assert swap_List([4, 5, 6]) == [6, 5, 4]

check(swap_List)