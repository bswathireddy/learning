#opened t10.dat file in pycharm and saved to my project path ie.pycharam\DATA200Assignment\venv folder and then reading file
#reading the file by opening t10.dat file from my directory
#splitting and converting to array
#initialized an empty array and looped through that array to convert string to int
#calling printHistogram method to get an output of histogram for given input
#created histogram method and written code to get output without using hist() library.
def firstAssignment():
    f = open("t10.dat", "r")
    line = f.read()
    array = line.split()
    array1 = []
    for k in range(len(array)):
        t = int(array[k])
        array1.append(t)
    printHistogram(array1)
def printHistogram(nums):
    maximum=max(nums)
    min=0
    dict1={}
    for l in range(maximum,-1,-1):
        dict1.update({l:''})
    for i in range(0,len(nums)):
        if nums[i] not in dict1:
            dict1.update({nums[i]:'X'})
        else:
            x=dict1.get(nums[i])
            x+='X'
            dict1.update({nums[i]:x})
    # iterating through dictionary
    for j in dict1:
        print(j,dict1.get(j))


firstAssignment()
