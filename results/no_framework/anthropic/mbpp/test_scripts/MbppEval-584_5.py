import re

def find_adverbs(text):
    """
    Write a function to find the first adverb ending with ly and its positions in a given string.

    Examples:
    find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    find_adverbs("Complete the task quickly") == '18-25: quickly'
    """
    # Use a regular expression to find the first adverb ending with 'ly'
    match = re.search(r'\b\w+ly\b', text)
    if match:
        # Get the matched adverb and its start and end positions
        adverb = match.group()
        start = match.start()
        end = match.end()
        return f'{start}-{end}: {adverb}'
    else:
        return None

def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)