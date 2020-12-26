dict1 = {1: 1, 2: 2}
def climbStairs(n):
    if n in dict1:
        return dict1.get(n)
    store = climbStairs(n - 1) + climbStairs(n - 2)
    dict1.update({n: store})
    return store


print(climbStairs(7))