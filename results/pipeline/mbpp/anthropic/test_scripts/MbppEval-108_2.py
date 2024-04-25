import heapq

def merge_sorted_list(num1, num2, num3):
    result = []
    heap = []
    for num in num1:
        heapq.heappush(heap, num)
    for num in num2:
        heapq.heappush(heap, num)
    for num in num3:
        heapq.heappush(heap, num)
    while heap:
        result.append(heapq.heappop(heap))
    return result

def check(candidate):
    assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
    assert merge_sorted_list([1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12])==[1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 11, 12]
    assert merge_sorted_list([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1],[25, 35, 22, 85, 14, 65, 75, 25, 58],[12, 74, 9, 50, 61, 41])==[1, 2, 3, 4, 7, 8, 9, 9, 9, 10, 12, 14, 14, 18, 22, 25, 25, 35, 41, 50, 58, 61, 65, 74, 75, 85]

check(merge_sorted_list)