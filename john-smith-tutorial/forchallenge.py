numbers=[5,2,5,2,2]
 for count in numbers:
    print('x'*count)


numbers=[5,2,5,2,5]
for count in numbers:
    output=''
    for x_count in range(count):
        output+='x'
    print(output)