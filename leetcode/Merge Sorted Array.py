def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    s = len(nums1) - 1
    while (n > 0 and m > 0):
        if nums1[m - 1] < nums2[n - 1]:
            nums1[s] = nums2[n - 1]
            n -= 1
        else:
            nums1[s] = nums1[m - 1]
            m -= 1
        s -= 1
    while n > 0:
        nums1[s] = nums2[n - 1]
        s -= 1
        n -= 1
    return nums1


print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))