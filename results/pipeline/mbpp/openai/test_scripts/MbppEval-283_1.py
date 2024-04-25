def validate(n): 
    '''
    Write a python function that takes in an integer and checks whether the frequency of each digit in the integer is 
    less than or equal to the digit itself.

    Examples:
    validate(1234) == True
    validate(51241) == False
    validate(321) == True
    '''
    num_str = str(n)
    digit_freq = {}

    for digit in num_str:
        if digit in digit_freq:
            digit_freq[digit] += 1
        else:
            digit_freq[digit] = 1

    for digit, freq in digit_freq.items():
        if int(digit) < freq:
            return False
    
    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)