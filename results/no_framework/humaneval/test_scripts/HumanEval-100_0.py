def make_a_pile(n):
    stones = []
    stones.append(n)
    
    current_stones = n
    for i in range(1, n):
        if current_stones % 2 == 0:
            current_stones += 1
        else:
            current_stones += 2
        stones.append(current_stones)
    
    return stones

# Test the function with the example


def check(candidate):

    # Check some simple cases
    assert candidate(3) == [3, 5, 7], "Test 3"
    assert candidate(4) == [4,6,8,10], "Test 4"
    assert candidate(5) == [5, 7, 9, 11, 13]
    assert candidate(6) == [6, 8, 10, 12, 14, 16]
    assert candidate(8) == [8, 10, 12, 14, 16, 18, 20, 22]

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(make_a_pile)