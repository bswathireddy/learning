def move_zeros(nums):
    p1 = 0
    p2 = 0
    while p2 < len(nums):
        if nums[p1] != 0 and nums[p2] != 0:
            p1 += 1
            p2 += 1
        else:
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                nums[p2] = 0
                p1 += 1
            p2 += 1
    return nums


print(move_zeros([0, 1, 0, 3, 12]))


