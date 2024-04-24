def reverse_string_list(stringlist):
    reversed_list = [string[::-1] for string in stringlist]
    return reversed_list

# Test the function
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
assert reverse_string_list(['john','amal','joel','george']) == ['nhoj','lama','leoj','egroeg']
assert reverse_string_list(['jack','john','mary']) == ['kcaj','nhoj','yram']



def check(candidate):
    assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
    assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']

check(reverse_string_list)