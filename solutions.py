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

    Ransom Note:
    - create hashmaps for both strings
    - iterate through strings and store number letters in each
    - return False if number of particular letter in magazine is less than in ransom note

    **Intervals**

    Summary Range:
    - iterate through array
    - if at last element of array, append range to list
    - if not at last element and next element is consecutive, continue
    - if not at last element and next element is not consecutive (ie. [..., 6, 8,..]), 
        append range to array and set start as next element (ie. start = 8)

    **Stack**

    Valid Parentheses:
    - create dictionary mapping closing parentheses to open ones
    - iterate through string, if find open parentheses, push to stack
    - if find closing, check if open version is at top of stack, if so pop from stack, if not return false 
    - return true of stack is empty by end of loop, else false
    '''


print(x)