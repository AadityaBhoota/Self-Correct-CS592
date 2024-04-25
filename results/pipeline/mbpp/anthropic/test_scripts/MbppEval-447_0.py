def cube_nums(nums):
    cubed_nums = []
    for num in nums:
        cubed_nums.append(num ** 3)
    return cubed_nums

def check(candidate):
    assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    assert cube_nums([10,20,30])==([1000, 8000, 27000])
    assert cube_nums([12,15])==([1728, 3375])

check(cube_nums)