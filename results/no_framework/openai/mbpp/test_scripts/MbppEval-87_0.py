def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    merged_dict.update(dict3)
    return merged_dict

# Test the function with the provided examples



def check(candidate):
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{"L":"lavender","B":"Blue"})=={'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" },{"L":"lavender","B":"Blue"},{ "G": "Green", "W": "White" })=={'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 'L': 'lavender', 'W': 'White'}

check(merge_dictionaries_three)