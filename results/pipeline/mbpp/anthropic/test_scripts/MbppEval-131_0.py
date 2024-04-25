def reverse_vowels(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_list = list(str1)
    
    # Find the indices of the vowels
    vowel_indices = [i for i, char in enumerate(char_list) if char.lower() in vowels]
    
    # Reverse the vowels
    for i in range(len(vowel_indices) // 2):
        char_list[vowel_indices[i]], char_list[vowel_indices[len(vowel_indices) - 1 - i]] = char_list[vowel_indices[len(vowel_indices) - 1 - i]], char_list[vowel_indices[i]]
    
    return ''.join(char_list)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)