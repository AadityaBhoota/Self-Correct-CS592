def reverse_Array_Upto_K(input_array, k):
    """
    Write a python function to reverse an array upto a given position.

    Examples:
    reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]
    """
    # Reverse the array up to the given position
    input_array[:k] = input_array[k-1::-1]
    return input_array

def check(candidate):
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]

check(reverse_Array_Upto_K)