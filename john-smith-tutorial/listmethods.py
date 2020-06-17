numbers=[3,4,5,6,7]
print(numbers.append(8))
print(numbers.index(5))
integers=[3,4,3,5]
print(integers.insert(0,2))
print(integers.remove(4))
print(integers.pop())
print(integers.clear())
print(50 in integers)
print(integers.count(3))
print(integers.sort())#result is none so use like this:
integers.sort()
print(integers)#gives asccending order list
integers.reverse()#gives descending odered list
print(integers)
integers2=integers.copy()#to copy the first list digits and do not effect it
integers.append(10)
print(integers2)

