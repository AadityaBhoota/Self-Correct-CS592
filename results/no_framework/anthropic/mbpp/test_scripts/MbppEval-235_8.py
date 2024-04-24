def even_bit_set_number(n):
    """
    Write a python function to set all even bits of a given number.

    Examples:
    even_bit_set_number(10) == 10
    even_bit_set_number(20) == 30
    even_bit_set_number(30) == 30
    """
    # Convert the number to binary
    binary_str = bin(n)[2:]

    # Iterate through the binary string and set the even bits to 1
    result = ''
    for i, bit in enumerate(binary_str[::-1]):
        if (i+1) % 2 == 0:
            result = '1' + result
        else:
            result = bit + result

    # Convert the result back to an integer and return it
    return int(result, 2)

def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)