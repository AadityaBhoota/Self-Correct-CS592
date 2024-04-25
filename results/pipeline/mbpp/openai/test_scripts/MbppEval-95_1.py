def Find_Min_Length(lst):  
    min_length = len(lst[0])
    
    for inner_lst in lst:
        if len(inner_lst) < min_length:
            min_length = len(inner_lst)
    
    return min_length

def check(candidate):
    assert Find_Min_Length([[1],[1,2]]) == 1
    assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3

check(Find_Min_Length)