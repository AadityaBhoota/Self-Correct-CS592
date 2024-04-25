def interleave_lists(list1, list2, list3):
    if len(list1) == len(list2) == len(list3):
        result = []
        for i in range(len(list1)):
            result.append(list1[i])
            result.append(list2[i])
            result.append(list3[i])
        return result
    else:
        return "Error: All lists must be of the same length."

def check(candidate):
    assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
    assert interleave_lists([10,20],[15,2],[5,10])==[10,15,5,20,2,10]
    assert interleave_lists([11,44], [10,15], [20,5])==[11,10,20,44,15,5]

check(interleave_lists)