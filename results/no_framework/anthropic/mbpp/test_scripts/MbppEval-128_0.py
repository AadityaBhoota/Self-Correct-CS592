def long_words(n, str):
    """
    Write a function to find words that are longer than n characters from a given list of words.

    Examples:
    long_words(3, "python is a programming language") == ['python', 'programming', 'language']
    long_words(2, "writing a program") == ['writing', 'program']
    long_words(5, "sorting list") == ['sorting']
    """
    # Split the input string into a list of words
    words = str.split()
    
    # Create a new list containing only the words longer than n characters
    longer_words = [word for word in words if len(word) > n]
    
    return longer_words

def check(candidate):
    assert long_words(3,"python is a programming language")==['python','programming','language']
    assert long_words(2,"writing a program")==['writing','program']
    assert long_words(5,"sorting list")==['sorting']

check(long_words)