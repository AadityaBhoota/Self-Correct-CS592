def is_bored(S):
    sentences = S.split('.')
    sentences = [s.strip() for s in sentences if s]
    
    count = 0
    for sentence in sentences:
        if sentence.startswith('I'):
            count += 1
    
    return count

# Test cases



def check(candidate):

    # Check some simple cases
    assert candidate("Hello world") == 0, "Test 1"
    assert candidate("Is the sky blue?") == 0, "Test 2"
    assert candidate("I love It !") == 1, "Test 3"
    assert candidate("bIt") == 0, "Test 4"
    assert candidate("I feel good today. I will be productive. will kill It") == 2, "Test 5"
    assert candidate("You and I are going for a walk") == 0, "Test 6"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(is_bored)