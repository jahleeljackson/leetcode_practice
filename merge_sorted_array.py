def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            nums1[m + i] = nums2[i]
        nums1.sort()
        return nums1


if __name__ == "__main__":
      nums1 = [1, 2, 3, 0, 0, 0]
      nums2 = [2, 5, 6]
      print(merge(nums1, 3, nums2, 3))