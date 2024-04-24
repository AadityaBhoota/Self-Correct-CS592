def specialFilter(nums):
    count = 0
    for num in nums:
        # Convert the number to an absolute value to handle negative numbers
        num = abs(num)
        # Check if the number is greater than 10
        if num > 10:
            # Extract the first and last digits
            first_digit = int(str(num)[0])
            last_digit = int(str(num)[-1])
            # Check if the first and last digits are odd
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

def check(candidate):

    # Check some simple cases
    assert candidate([5, -2, 1, -5]) == 0  
    assert candidate([15, -73, 14, -15]) == 1
    assert candidate([33, -2, -3, 45, 21, 109]) == 2
    assert candidate([43, -12, 93, 125, 121, 109]) == 4
    assert candidate([71, -2, -33, 75, 21, 19]) == 3


    # Check some edge cases that are easy to work out by hand.
    assert candidate([1]) == 0              
    assert candidate([]) == 0                   


check(specialFilter)