def large_product(nums1, nums2, N):
    # Create a list of all possible products
    products = [a * b for a in nums1 for b in nums2]
    
    # Sort the products in descending order
    products.sort(reverse=True)
    
    # Return the first N elements of the sorted products list
    return products[:N]

def check(candidate):
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
    assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]

check(large_product)