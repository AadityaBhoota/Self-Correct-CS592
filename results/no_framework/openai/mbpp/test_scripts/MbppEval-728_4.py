def sum_list(lst1, lst2):
    return [a + b for a, b in zip(lst1, lst2)]

# Test the function with examples




def check(candidate):
    assert sum_list([10,20,30],[15,25,35])==[25,45,65]
    assert sum_list([1,2,3],[5,6,7])==[6,8,10]
    assert sum_list([15,20,30],[15,45,75])==[30,65,105]

check(sum_list)