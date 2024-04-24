from collections import Counter

def sort_counter(dict1):
    # Sort the dictionary items by value in descending order
    sorted_items = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_items

# Test the function




def check(candidate):
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
    assert sort_counter({'Math':400, 'Physics':300, 'Chemistry':250})==[('Math', 400), ('Physics', 300), ('Chemistry', 250)]
    assert sort_counter({'Math':900, 'Physics':1000, 'Chemistry':1250})==[('Chemistry', 1250), ('Physics', 1000), ('Math', 900)]

check(sort_counter)