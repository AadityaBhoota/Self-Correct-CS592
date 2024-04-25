def search(arr):
    index = 0
    n = len(arr)
    
    while index < n:
        if index == n - 1 or arr[index] != arr[index + 1]:
            return arr[index]
        
        index += 2

def check(candidate):
    assert search([1,1,2,2,3]) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert search([1,2,2,3,3,4,4]) == 1

check(search)