def all_unique(test_list):
    unique_set = set()
    
    for elem in test_list:
        if elem in unique_set:
            return False
        unique_set.add(elem)
    
    return True

def check(candidate):
    assert all_unique([1,2,3]) == True
    assert all_unique([1,2,1,2]) == False
    assert all_unique([1,2,3,4,5]) == True

check(all_unique)