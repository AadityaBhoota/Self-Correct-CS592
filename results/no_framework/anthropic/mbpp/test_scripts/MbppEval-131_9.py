def reverse_vowels(str1):
    """
    Write a python function to reverse only the vowels of a given string (where y is not a vowel).

    Examples:
    reverse_vowels("Python") == "Python"
    reverse_vowels("USA") == "ASU"
    reverse_vowels("ab") == "ab"
    """
    vowels = "aeiou"
    str_list = list(str1)
    i, j = 0, len(str_list) - 1

    while i < j:
        if str_list[i].lower() in vowels and str_list[j].lower() in vowels:
            str_list[i], str_list[j] = str_list[j], str_list[i]
            i += 1
            j -= 1
        elif str_list[i].lower() in vowels:
            j -= 1
        else:
            i += 1

    return "".join(str_list)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)