def check_tuplex(tuplex, element):
    return element in tuplex

# Testing the function




def check(candidate):
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'5')==False
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c","e"),3)==True

check(check_tuplex)