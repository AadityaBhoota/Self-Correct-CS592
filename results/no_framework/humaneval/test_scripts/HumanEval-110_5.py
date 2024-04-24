def exchange(lst1, lst2):
    # Count the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # Count the number of odd elements in lst2
    odd_count += sum(1 for num in lst2 if num % 2 != 0)
    
    # If the total count of odd elements is even, it means we can exchange elements to make lst1 all even
    if odd_count % 2 == 0:
        return "YES"
    else:
        return "NO"

# Test cases



def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert candidate([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert candidate([1, 2, 3, 4], [2, 1, 4, 3]) == "YES" 
    assert candidate([5, 7, 3], [2, 6, 4]) == "YES"
    assert candidate([5, 7, 3], [2, 6, 3]) == "NO" 
    assert candidate([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1]) == "NO"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([100, 200], [200, 200]) == "YES"


check(exchange)