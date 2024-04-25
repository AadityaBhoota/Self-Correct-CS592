def is_sublist(l, s):
    start = 0
    for item in l:
        if item == s[start]:
            start += 1
            if start == len(s):
                return True
    return False

def check(candidate):
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False

check(is_sublist)