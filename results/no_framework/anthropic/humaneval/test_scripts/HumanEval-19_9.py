from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map the written words to their corresponding integers
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of written numbers
    written_nums = numbers.split()
    
    # Convert the written numbers to their corresponding integers
    int_nums = [num_dict[num] for num in written_nums]
    
    # Sort the integers in ascending order
    int_nums.sort()
    
    # Convert the sorted integers back to their written form
    sorted_written_nums = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in int_nums]
    
    # Join the sorted written numbers back into a string
    return ' '.join(sorted_written_nums)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('three') == 'three'
    assert candidate('three five nine') == 'three five nine'
    assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
    assert candidate('six five four three two one zero') == 'zero one two three four five six'

check(sort_numbers)