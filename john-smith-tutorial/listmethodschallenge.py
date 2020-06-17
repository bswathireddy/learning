# write a program to remove duplicates in the list
numbers=[2,8,9,7,8,9]
output=[]
for number in numbers:
    if number not in output:
        output.append(number)
print(output)

