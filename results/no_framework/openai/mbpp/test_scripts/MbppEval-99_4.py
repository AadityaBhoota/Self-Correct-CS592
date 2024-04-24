def decimal_to_binary(n):
    if n == 0:
        return '0'
    
    binary = ''
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return binary

# Test cases




def check(candidate):
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111'

check(decimal_to_binary)