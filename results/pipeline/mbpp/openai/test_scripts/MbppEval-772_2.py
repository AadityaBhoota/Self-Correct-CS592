def remove_length(test_str, K):
    words = test_str.split()
    filtered_words = [word for word in words if len(word) != K]
    filtered_str = ' '.join(filtered_words)
    return filtered_str

def check(candidate):
    assert remove_length('The person is most value tet', 3) == 'person is most value'
    assert remove_length('If you told me about this ok', 4) == 'If you me about ok'
    assert remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'

check(remove_length)