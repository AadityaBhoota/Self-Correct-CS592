def Diff(li1, li2):
    set1 = set(li1)
    set2 = set(li2)
    
    diff_set = set1.difference(set2)
    
    diff_list = list(diff_set)
    
    return diff_list

def check(candidate):
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
    assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
    assert (Diff([1,2,3], [6,7,1])) == [2,3,6,7]

check(Diff)