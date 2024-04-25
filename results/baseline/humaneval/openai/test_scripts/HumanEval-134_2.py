def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    
    last_char = txt[-1]
    
    if last_char.isalpha():
        if len(txt) == 1:
            return True
        elif txt[-2] == ' ':
            return True
        else:
            return False
    else:
        return False

# Test cases





def check(candidate):

    # Check some simple cases
    assert candidate("apple") == False
    assert candidate("apple pi e") == True
    assert candidate("eeeee") == False
    assert candidate("A") == True
    assert candidate("Pumpkin pie ") == False
    assert candidate("Pumpkin pie 1") == False
    assert candidate("") == False
    assert candidate("eeeee e ") == False
    assert candidate("apple pie") == False
    assert candidate("apple pi e ") == False

    # Check some edge cases that are easy to work out by hand.
    assert True


check(check_if_last_char_is_a_letter)