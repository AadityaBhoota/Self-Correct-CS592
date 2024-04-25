def all_Characters_Same(s):
    unique_chars = set()
    for char in s:
        unique_chars.add(char)
    return len(unique_chars) == 1

def check(candidate):
    assert all_Characters_Same("python") == False
    assert all_Characters_Same("aaa") == True
    assert all_Characters_Same("data") == False

check(all_Characters_Same)