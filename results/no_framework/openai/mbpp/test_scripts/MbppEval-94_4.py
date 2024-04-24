def index_minimum(test_list):
    min_tuple = min(test_list, key=itemgetter(1))
    return min_tuple[0]

# Testing the function with example inputs




def check(candidate):
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'

check(index_minimum)