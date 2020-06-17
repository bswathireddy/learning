
# arr=[1,3,4,7,10,20,98,121]
# key =0
# output=-1
# mid=-1
# start=0
# end=len(arr)-1
# #write program to do binary search on arr.append. output if key =7 is 3
# #assign start =0 end = length-1, middle = start+end/2
# #write a while loop
# while(end>=start):
#     mid=int((start+end)/2)
#     if arr[mid]==key:
#         output=mid
#         break
#     if arr[mid]<key:
#         start=mid+1
#     if arr[mid]>key:
#         end=mid-1
# print(output)

arr=[1,1,1,1,1]
output=len(arr)
mid=-1
start=0
end=len(arr)-1
while(end>=start):
    mid=int((start+end)/2)
    if arr[mid]==0:
        if mid-1>=0 and arr[mid]==arr[mid-1]:
            end=mid-1
        else:
            output=mid
            break
    else:
        start=mid+1
print(len(arr)-output)



