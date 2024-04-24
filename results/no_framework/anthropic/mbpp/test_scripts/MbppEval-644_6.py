def reverse_Array_Upto_K(input_list, k):
    """
    Reverses the first k elements of the input list.
    
    Args:
    input_list (list): The input list to be reversed.
    k (int): The position up to which the list should be reversed.
    
    Returns:
    list: The modified list with the first k elements reversed.
    """
    if k > len(input_list):
        raise ValueError("k cannot be greater than the length of the input list")
    
    # Reverse the first k elements
    input_list[:k] = input_list[k-1::-1]
    
    return input_list

def check(candidate):
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]

check(reverse_Array_Upto_K)