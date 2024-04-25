def freq_count(list1):
    freq_dict = {}  # Step 1: Create an empty dictionary to store frequency count
    
    for element in list1:  # Step 2: Loop through each element in the list
        if element in freq_dict:  # Step 3: Check if element is already in dictionary
            freq_dict[element] += 1  # Step 4: Increment the count for existing element
        else:
            freq_dict[element] = 1  # Step 5: Add element to dictionary with count of 1

    return freq_dict  # Step 6: Return the dictionary with frequency count

def check(candidate):
    assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
    assert freq_count([1,2,3,4,3,2,4,1,3,1,4])==({1:3, 2:2,3:3,4:3})
    assert freq_count([5,6,7,4,9,10,4,5,6,7,9,5])==({10:1,5:3,6:2,7:2,4:2,9:2})

check(freq_count)