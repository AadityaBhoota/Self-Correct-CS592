def count_samepair(list1, list2, list3):
    count = 0
    min_length = min(len(list1), len(list2), len(list3))

    for i in range(min_length):
        if list1[i] == list2[i] == list3[i]:
            count += 1

    return count

# Test cases




def check(candidate):
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==4
    assert count_samepair([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==5

check(count_samepair)