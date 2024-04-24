def count_reverse_pairs(test_list):
    reverse_pairs = 0
    for i in range(len(test_list)):
        for j in range(i+1, len(test_list)):
            if test_list[i][::-1] == test_list[j]:
                reverse_pairs += 1
    return str(reverse_pairs)

# Test cases




def check(candidate):
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
    assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1
    assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2

check(count_reverse_pairs)