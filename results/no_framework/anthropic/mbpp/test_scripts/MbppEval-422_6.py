def find_Average_Of_Cube(n):
    """
    Write a python function to find the average of cubes of first n natural numbers.

    Examples:
    find_Average_Of_Cube(2) == 4.5
    find_Average_Of_Cube(3) == 12
    find_Average_Of_Cube(1) == 1
    """
    if n <= 0:
        return 0
    
    total_sum = sum(i**3 for i in range(1, n+1))
    average = total_sum / n
    
    return average

def check(candidate):
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(3) == 12
    assert find_Average_Of_Cube(1) == 1

check(find_Average_Of_Cube)