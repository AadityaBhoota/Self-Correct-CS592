def find_Average_Of_Cube(n):
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    average = sum_of_cubes / n
    return average

def check(candidate):
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(3) == 12
    assert find_Average_Of_Cube(1) == 1

check(find_Average_Of_Cube)