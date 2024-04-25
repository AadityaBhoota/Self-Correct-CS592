def extract_index_list(l1, l2, l3):
    result = []
    for i in range(len(l1)):
        if l1[i] == l2[i] == l3[i]:
            result.append(l1[i])
    return result

def check(candidate):
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 6, 5],[0, 1, 2, 3, 4, 6, 7])==[1, 6]
    assert extract_index_list([1, 1, 3, 4, 6, 5, 6],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 5]
    assert extract_index_list([1, 2, 3, 4, 6, 6, 6],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[]

check(extract_index_list)