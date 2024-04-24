def cycpattern_check(a, b):
    if len(a) != len(b):
        return False

    a += a   # Double the first word for easier rotation checking
    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] == b:
            return True

    return False

# Test cases







def check(candidate):

    # Check some simple cases
    #assert True, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    #assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert  candidate("xyzw","xyw") == False , "test #0"
    assert  candidate("yello","ell") == True , "test #1"
    assert  candidate("whattup","ptut") == False , "test #2"
    assert  candidate("efef","fee") == True , "test #3"
    assert  candidate("abab","aabb") == False , "test #4"
    assert  candidate("winemtt","tinem") == True , "test #5"


check(cycpattern_check)