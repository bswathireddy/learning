def intersection(nums1, nums2):
    output = []
    i = 0
    while i <= len(nums1)-1:
        for j in nums2:
            if nums1[i] == j:
                if j not in output:
                    output.append(j)
                else:
                    continue

        i += 1
    return output


print(intersection([1],[1]))