def text_starta_endb(text):
    if re.search(r'a.*b$', text):
        return 'Found a match!'
    else:
        return 'Not matched'

# Testing the function




def check(candidate):
    assert text_starta_endb("aabbbb")
    assert not text_starta_endb("aabAbbbc")
    assert not text_starta_endb("accddbbjjj")

check(text_starta_endb)