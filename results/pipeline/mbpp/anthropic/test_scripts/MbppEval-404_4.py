def minimum(a, b):
    if a <= b:
        return a
    else:
        return b

def check(candidate):
    assert minimum(1,2) == 1
    assert minimum(-5,-4) == -5
    assert minimum(0,0) == 0

check(minimum)