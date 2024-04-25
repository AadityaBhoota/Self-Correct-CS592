def re_arrange_array(arr, n):
    neg_elements = []
    pos_elements = []
    
    for num in arr[:n]:
        if num < 0:
            neg_elements.append(num)
        else:
            pos_elements.append(num)
    
    re_arranged_arr = neg_elements + pos_elements
    
    return re_arranged_arr

def check(candidate):
    assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
    assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
    assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]

check(re_arrange_array)