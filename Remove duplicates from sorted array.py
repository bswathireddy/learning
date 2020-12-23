def removeDuplicates(nums):
    p1 = 0
    p2 = 1
    while p2<=(len(nums) - 1):
        if nums[p1] == nums[p2]:
            r = nums[p2]
            nums.remove(r)
        else:
            p1 +=
            p2 += 1
    return len(nums)


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))