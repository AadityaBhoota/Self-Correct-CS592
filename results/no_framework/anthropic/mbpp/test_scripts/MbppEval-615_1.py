def average_tuple(nums):
    """
    Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.

    Examples:
    average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))) == [30.5, 34.25, 27.0, 23.25]
    average_tuple(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))) == [25.5, -18.0, 3.75]
    average_tuple(((100, 100, 100, 120), (300, 450, 560, 450), (810, 800, 390, 320), (10, 20, 30, 40))) == [305.0, 342.5, 270.0, 232.5]
    """
    result = []
    for t in nums:
        avg = sum(t) / len(t)
        result.append(avg)
    return result

def check(candidate):
    assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
    assert average_tuple(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3)))== [25.5, -18.0, 3.75]
    assert average_tuple( ((100, 100, 100, 120), (300, 450, 560, 450), (810, 800, 390, 320), (10, 20, 30, 40)))==[305.0, 342.5, 270.0, 232.5]

check(average_tuple)