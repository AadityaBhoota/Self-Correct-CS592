def check_monthnumb_number(monthnum):
    thirty_one_days = [1, 3, 5, 7, 8, 10, 12]

    if monthnum in thirty_one_days:
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False

check(check_monthnumb_number)