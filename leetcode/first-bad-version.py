def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    start = 0
    end = n
    while start <= end:
        mid = int((start + end) / 2)
        if isBadVersion(mid) == True:
            end = mid - 1
            if isBadVersion(end) != True:
                return mid
        if isBadVersion(mid) == False:
            start = mid + 1
