def return_sum(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total

def check(candidate):
    assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
    assert return_sum({'a': 25, 'b':18, 'c':45}) == 88
    assert return_sum({'a': 36, 'b':39, 'c':49}) == 124

check(return_sum)