from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")
    
    min_value = min(numbers)
    max_value = max(numbers)
    
    if min_value == max_value:
        return [0.0] * len(numbers)
    
    return [(x - min_value) / (max_value - min_value) for x in numbers]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([2.0, 49.9]) == [0.0, 1.0]
    assert candidate([100.0, 49.9]) == [1.0, 0.0]
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert candidate([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
    assert candidate([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]

check(rescale_to_unit)