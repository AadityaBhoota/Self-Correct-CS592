import re

def text_match_one(text):
    # pattern to match 'a' followed by one or more 'b's
    pattern = 'ab+'
    
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# Test cases




def check(candidate):
    assert text_match_one("ac")==False
    assert text_match_one("dc")==False
    assert text_match_one("abba")==True

check(text_match_one)