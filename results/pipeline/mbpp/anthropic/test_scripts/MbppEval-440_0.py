import re

def find_adverb_position(text):
    pattern = r'^\w*?(\w+ly)\b\w*'
    match = re.search(pattern, text)
    if match:
        start = match.start()
        end = match.end()
        adverb = match.group(1)
        return (start, end, adverb)
    else:
        return None

def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

check(find_adverb_position)