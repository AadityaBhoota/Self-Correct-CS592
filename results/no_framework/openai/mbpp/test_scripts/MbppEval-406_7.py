def find_parity(x):
    if x % 2 == 0:
        return "Even Parity"
    else:
        return "Odd Parity"

# Test cases




def check(candidate):
    assert find_Parity(12) == False
    assert find_Parity(7) == True
    assert find_Parity(10) == False

check(find_Parity)