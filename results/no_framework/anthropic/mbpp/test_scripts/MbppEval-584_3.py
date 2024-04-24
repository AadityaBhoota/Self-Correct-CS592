import re

def find_adverbs(text):
    """
    Write a function to find the first adverb ending with ly and its positions in a given string.

    Examples:
    find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    find_adverbs("Complete the task quickly") == '18-25: quickly'
    """
    pattern = r'\w+ly'
    match = re.search(pattern, text)
    if match:
        start = match.start()
        end = match.end()
        adverb = text[start:end]
        return f'{start}-{end}: {adverb}'
    else:
        return ''

def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)