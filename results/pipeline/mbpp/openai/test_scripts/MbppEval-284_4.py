def check_element(list, element):
    for item in list:
        if item != element:
            return False

    return True

def check(candidate):
    assert check_element(["green", "orange", "black", "white"],'blue')==False
    assert check_element([1,2,3,4],7)==False
    assert check_element(["green", "green", "green", "green"],'green')==True

check(check_element)