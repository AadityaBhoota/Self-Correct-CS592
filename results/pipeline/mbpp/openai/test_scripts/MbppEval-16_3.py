import re

def text_lowercase_underscore(text):
    if re.search(r'\b[a-z]+_[a-z]+\b', text):
        return 'Found a match!'
    else:
        return 'Not matched!'

def check(candidate):
    assert text_lowercase_underscore("aab_cbbbc")==(True)
    assert text_lowercase_underscore("aab_Abbbc")==(False)
    assert text_lowercase_underscore("Aaab_abbbc")==(False)

check(text_lowercase_underscore)