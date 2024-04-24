def number_of_substrings(s):
    """
    Write a python function to count the number of non-empty substrings of a given string.

    Examples:
    number_of_substrings("abc") == 6
    number_of_substrings("abcd") == 10
    number_of_substrings("abcde") == 15
    """
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            count += 1
    return count

def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)