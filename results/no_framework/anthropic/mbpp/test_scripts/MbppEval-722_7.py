def filter_data(students, h, w):
    """
    Filters the dictionary of students based on the minimum height and weight criteria.

    Args:
        students (dict): A dictionary with student names as keys and (height, weight) tuples as values.
        h (float): The minimum height requirement.
        w (float): The minimum weight requirement.

    Returns:
        dict: A new dictionary containing only the students who meet the height and weight criteria.
    """
    return {student: (height, weight) for student, (height, weight) in students.items() if height >= h and weight >= w}

def check(candidate):
    assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
    assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},5.9,67)=={'Cierra Vega': (6.2, 70),'Kierra Gentry': (6.0, 68)}
    assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},5.7,64)=={'Cierra Vega': (6.2, 70),'Alden Cantrell': (5.9, 65),'Kierra Gentry': (6.0, 68),'Pierre Cox': (5.8, 66)}

check(filter_data)