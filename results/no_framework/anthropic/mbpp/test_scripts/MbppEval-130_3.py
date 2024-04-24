from collections import defaultdict

def max_occurrences(nums):
    """
    Write a function to find the item with maximum frequency in a given list.

    Examples:
    max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == (2, 5)
    max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,16,18]) == (8, 2)
    max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10]) == (20, 3)
    """
    # Create a defaultdict to store the frequency of each item
    freq = defaultdict(int)

    # Count the frequency of each item
    for num in nums:
        freq[num] += 1

    # Find the item with the maximum frequency
    max_count = 0
    max_item = None
    for item, count in freq.items():
        if count > max_count:
            max_count = count
            max_item = item

    return max_item, max_count

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20

check(max_occurrences)