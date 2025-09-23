x =  '''
    **Strings/Arrays**

    Merge Sorted Array:
    - append nums2 to nums1
    - sort using nums1.sort()

    **Two Pointers**

    Is Subsequence:
    - iterate through long string
    - only iterate pointer of short string if there is match
    - return False if reach end of for loop without all of short string being validated

    **Sliding Window**

    Minimum Subsize Array Sum:
    - iterate through array changing window length based on sum 
    - increase array length (right pointer++) if sum is < than target
    - decrease array length (left pointer++) if sum is >= target
    - track the smallest window length and return that 

    **Matrix**

    Valid Sudoku:
    - use hashsets to confirm validity: rows, columns, and boxs
    - iterate through every element of board ([rows][cols] double nested for loop)
    - define boxes as coordinates with integer division
    - if element exists in any of the hashsets at a key value, return false

    **Hashmap**

    
    '''


print(x)