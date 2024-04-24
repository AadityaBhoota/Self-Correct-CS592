def min_k(test_list, K):
    """
    Write a function to find minimum k records from tuple list.
    """
    test_list.sort(key=lambda x: x[1])  # Sort the list based on the second element of each tuple
    return test_list[:K]  # Return the first K elements of the sorted list

# Examples:




def check(candidate):
    assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
    assert min_k([('Sanjeev', 11), ('Angat', 5), ('Akash', 3), ('Nepin', 9)], 3) == [('Akash', 3), ('Angat', 5), ('Nepin', 9)]
    assert min_k([('tanmay', 14), ('Amer', 11), ('Ayesha', 9), ('SKD', 16)], 1) == [('Ayesha', 9)]

check(min_k)