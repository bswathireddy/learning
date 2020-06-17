s='asdfghjkl;poiuusdfgjkfdsa'
temp=[]
output=-1
for i in s:
    if i in temp:
        if output==-1 or temp.index(i) < temp.index(output):
            output = i
    else:
        if output == -1:
            temp.append(i)

print(output)