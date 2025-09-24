def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """

    if len(nums) == 0:
        return []

    res = []

    start = nums[0]

    for i in range(len(nums)):
        if i == len(nums) - 1:
            res.append(str(start) + "->" + str(nums[i])) if start != nums[i] else res.append(str(nums[i]))
        elif i != len(nums) - 1 and nums[i + 1] == nums[i] + 1:
            continue
        else:
            res.append(str(start) + "->" + str(nums[i])) if start != nums[i] else res.append(str(nums[i]))
            start = nums[i + 1]

    return res




nums = [0,1,2,4,5,7]
print(summaryRanges(nums))