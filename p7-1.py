import os
'''Function to get input files.'''
'''Big O Notation of this getInputFiles function is O(n).'''

def getInputFiles():
    for file in os.listdir("."):
        if file.startswith("t7") and file.endswith(".dat"):
            try:
                if  os.path.getsize(file)==0:
                    raise TypeError("Input File is Empty")
                else:
                    print(file,':')
                    readingFile(file)
            except Exception as err:
                print("Error: "+file,err)
            finally:
                print("-----------")

'''Function to read lines from file.'''
'''Big O Notation of readingFile function is O(n).'''
def readingFile(filepath):
    with open(filepath) as f:
        lines=f.readlines()
        if len(lines)!=2:
            raise TypeError("Invalid Input")
        line2=[x.strip() for x in lines[1].split(",")]
        target=0
        try:
            target=int(lines[0])
        except:
            raise TypeError("Input is Invalid")
        if line2==None:
            raise TypeError("List does not exists")
        else:
            sumRelation(target,line2)

'''Function to find sum of all pairs that match or equal to target.'''
'''Declared dictionary to store all key value pairs.'''
'''Big O Notation of this main function is O(n).'''
def sumRelation(res,values):
    dictionary=dict()
    for i in range(0,len(values)):
        a=0
        try:
            a=int(values[i])
        except Exception:
            raise TypeError("Input is Invalid")
        b=str(res-(a))
        if b in dictionary:
            print(b,"+",a,"=",res)
            del dictionary[b]
        else:
            dictionary.update({values[i]:i})

    print(",".join(dictionary.keys()))


getInputFiles()


'''SOLUTION FOR PROBLEM 2: Big O Notation of given code is O(M^2.N). M=number of lists, N=Maximum elements in any list'''
