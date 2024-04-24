def max_product_tuple(list1):
    max_product = -1

    for tuple_pair in list1:
        product = abs(tuple_pair[0] * tuple_pair[1])
        if product > max_product:
            max_product = product

    return max_product

# Test cases




def check(candidate):
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
    assert max_product_tuple([(10,20), (15,2), (5,10)] )==200
    assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484

check(max_product_tuple)