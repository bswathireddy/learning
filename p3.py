'''This python program is to fine row-wise,column-wise and total sum by reading files with .dat from current directory by handling all the errors.'''
'''Importing os as we need to read files from directory.'''
import os
'''Defining a method to get input files of .dat extension by looping through given directory and calling readDataFile function.'''
#Big O Notation of this method is o(n) as am using for loop in this method to get files.
def getInputFiles():
    ext=".dat"
    for file in os.listdir("."):
        if file.startswith("t3") and file.endswith(ext):
            try:
                if os.path.getsize(file)==0:
                    raise TypeError("File is Empty")
                else:
                    readDataFile(file)
            except Exception as err:
                print("ERROR:"+file,err)
            finally:
                print("=======================")
'''Defining readDataFile and giving path as input.'''
'''Reading the input file and looping through the file to get the data from the file.'''
'''Looped through the each line in opened file to cumulate row-wise,colum-wise and total sum.'''
'''Raised errors if there is any white spaces ,negative integers or alphabets and thrown error to exception.'''
#Big O Notation of this method is o(nm) as it is looping through number of rows(n) and number of columns(m).
def readDataFile(filepath):
    with open(filepath) as f:
        colSum=None
        pre_len=None
        for line in f:
            a=line.split()
            if len(a)==0:
                continue
            if pre_len==None:
                pre_len=len(a)
            if len(a)!=pre_len:
                raise TypeError("Row Length mismatch")
                return
            if colSum==None:
                colSum=[0]*(len(a)+1)
            rowSum=0
            for i in range(len(a)):
                b=int(a[i])
                if(b<0):
                    raise TypeError('cannot handle negative numbers')
                rowSum+=b
                colSum[i]+=b
                print(b,end=' ')
            print(rowSum)
            colSum[len(a)]+=rowSum
        print(*colSum)


getInputFiles()



















































