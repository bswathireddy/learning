def singleNumber(nums):
    dic = dict()
    for i in range(0, len(nums)):
        if nums[i] not in dic:
            dic.update({nums[i]: 1})
        else:
            dic[nums[i]] += 1
    print(dic)
    for j in dic:
        s = dic.get(j)
        if s == 1:
            return j


print(singleNumber([4, 1, 2, 1, 2]))