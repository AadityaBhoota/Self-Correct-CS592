def reverse_words(s):
    '''
    Write a function to reverse words separated by spaces in a given string.

    Examples:
    reverse_words("python program") == ("program python")
    reverse_words("java language") == ("language java")
    reverse_words("indian man") == ("man indian")
    '''
    
    if not s:
        return ""
    
    words = s.split()
    reversed_words = words[::-1]
    reversed_string = " ".join(reversed_words)
    
    return reversed_string

def check(candidate):
    assert reverse_words("python program")==("program python")
    assert reverse_words("java language")==("language java")
    assert reverse_words("indian man")==("man indian")

check(reverse_words)