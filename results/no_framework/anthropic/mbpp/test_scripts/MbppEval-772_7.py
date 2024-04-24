def remove_length(test_str, K):
    """
    Write a function to remove all the words with k length in the given string.

    Examples:
    remove_length('The person is most value tet', 3) == 'person is most value'
    remove_length('If you told me about this ok', 4) == 'If you me about ok'
    remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'
    """
    # Split the input string into a list of words
    words = test_str.split()
    
    # Create a new list to store the words with length not equal to K
    new_words = [word for word in words if len(word) != K]
    
    # Join the words back into a string
    result = ' '.join(new_words)
    
    return result

def check(candidate):
    assert remove_length('The person is most value tet', 3) == 'person is most value'
    assert remove_length('If you told me about this ok', 4) == 'If you me about ok'
    assert remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'

check(remove_length)