def maximum(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a

def check(candidate):
    assert maximum(5,10) == 10
    assert maximum(-1,-2) == -1
    assert maximum(9,7) == 9

check(maximum)