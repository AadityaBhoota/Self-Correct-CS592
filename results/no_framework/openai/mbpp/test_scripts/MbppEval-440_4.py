import re

def find_adverb_position(text):
    adverb_match = re.search(r'\b[^\s]+ly\b', text, re.IGNORECASE)
    if adverb_match:
        adverb = adverb_match.group(0)
        start_index = adverb_match.start()
        end_index = adverb_match.end()
        return start_index, end_index, adverb
    return None

# Test the function with the provided examples




def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

check(find_adverb_position)