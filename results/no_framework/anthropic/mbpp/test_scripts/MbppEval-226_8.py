def odd_values_string(string):
    """
    Remove the characters which have odd index values from the given string.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with characters at odd indices removed.
    """
    return ''.join(char for i, char in enumerate(string) if i % 2 == 0)

def check(candidate):
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'
    assert odd_values_string('lambs') == 'lms'

check(odd_values_string)