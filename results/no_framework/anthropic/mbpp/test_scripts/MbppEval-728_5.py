def sum_list(lst1, lst2):
    """
    Write a function that takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].

    Examples:
    sum_list([10,20,30],[15,25,35]) == [25,45,65]
    sum_list([1,2,3],[5,6,7]) == [6,8,10]
    sum_list([15,20,30],[15,45,75]) == [30,65,105]
    """
    result = []
    for i in range(len(lst1)):
        result.append(lst1[i] + lst2[i])
    return result

def check(candidate):
    assert sum_list([10,20,30],[15,25,35])==[25,45,65]
    assert sum_list([1,2,3],[5,6,7])==[6,8,10]
    assert sum_list([15,20,30],[15,45,75])==[30,65,105]

check(sum_list)