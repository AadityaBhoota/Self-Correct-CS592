import re

def text_match_wordz_middle(text):
    pattern = r'\b\w*z\w*\b'
    if re.search(pattern, text):
        return "Found a match!"
    else:
        return "Not matched!"

def check(candidate):
    assert text_match_wordz_middle("pythonzabc.")==True
    assert text_match_wordz_middle("zxyabc.")==False
    assert text_match_wordz_middle("  lang  .")==False

check(text_match_wordz_middle)