def empty_dit(list1):
    for d in list1:
        if d:
            return False
    return True

# Test cases



def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)