def count_char_position(str1): 
    count = 0
    for i in range(len(str1)):
        char = str1[i].lower()
        if char.isalpha() and ord(char) - ord('a') == i:
            count += 1
    return count

# Test the function with examples




def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5

check(count_char_position)