def string_to_list(string):
    return string.split(' ')

def check(candidate):
    assert string_to_list("python programming")==['python','programming']
    assert string_to_list("lists tuples strings")==['lists','tuples','strings']
    assert string_to_list("write a program")==['write','a','program']

check(string_to_list)