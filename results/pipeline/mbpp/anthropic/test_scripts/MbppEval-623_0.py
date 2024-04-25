def nth_nums(nums, n):
    results = []
    for num in nums:
        results.append(num ** n)
    return results

def check(candidate):
    assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert nth_nums([10,20,30],3)==([1000, 8000, 27000])
    assert nth_nums([12,15],5)==([248832, 759375])

check(nth_nums)