def concatenate_tuple(test_tup):
    concatenated_str = ""

    for idx, elem in enumerate(test_tup):
        concatenated_str += str(elem)
        
        if idx < len(test_tup) - 1:
            concatenated_str += "-"
    
    return concatenated_str

def check(candidate):
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

check(concatenate_tuple)