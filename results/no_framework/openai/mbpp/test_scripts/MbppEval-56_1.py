def check(num):
    reverse_num = int(str(num)[::-1])
    if num == (2 * reverse_num) - 1:
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)