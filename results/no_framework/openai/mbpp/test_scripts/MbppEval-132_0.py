def tup_string(tup1):
    string = ''.join(tup1)
    return string

def check(candidate):
    assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
    assert tup_string(('p','y','t','h','o','n'))==("python")
    assert tup_string(('p','r','o','g','r','a','m'))==("program")

check(tup_string)