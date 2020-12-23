'''Importing os as am reading all files from os.listdir() '''
import os
'''Defined a method to get all input files. And looped through the current directory path to get files.'''
'''If a file is empty, catching and throwing exception'''
def getInputFiles():
    for file in os.listdir("."):
        if file.startswith("t5") and file.endswith(".dat"):
            try:
                if os.path.getsize(file)==0:
                    raise TypeError("file is empty")
                else:
                    evaluateEquation(file)
            except Exception as err:
                print("ERROR"+" "+file,err)
            finally:
                print("=======================")
'''Defined a method to perform mathematical operation which used as recursive to perform operations in main code.'''
def mathOperation(a,m,op):
    if op=="+":
        return a+m
    if op=="*":
        return a*m
'''Define a method for evaluateEquation. '''
'''Read file and looped through the input line to get characters in input.'''
'''Initialized two empty stacks to store the inputs, one stack is to store integers and one is to store operators.'''
'''Converting string to int.'''
'''Using append() pushed values into stack and using pop() brought integers out and performed mathematical operation.'''
def evaluateEquation(filepath):
    with open(filepath) as f:
        for line in f:
            stack=[]
            op=[]
            i=0
            while i<len(line):
                if line[i]==' ' or line[i]=='\t':
                    i+=1
                    continue
                if line[i]=="(":
                    op.append(line[i])
                elif line[i].isalpha():
                    raise TypeError("Given String has Alphabets")
                elif line[i].isdigit():
                    t=line[i]
                    j=i+1
                    while (j<len(line) and line[j].isdigit()):
                        t+=line[j]
                        j=j+1
                        i+=1
                    x=int(t)
                    stack.append(x)
                elif line[i]==")":
                    while len(op)!=0 and op[-1]!="(":
                        first=stack.pop()
                        second=stack.pop()
                        op1=op.pop()
                        stack.append(mathOperation(first,second,op1))
                    op.pop()
                elif line[i]=="*":
                    while len(op)!=0 and op[-1]=="*":
                        first=stack.pop()
                        second=stack.pop()
                        op1=op.pop()
                        stack.append(mathOperation(first,second,op1))
                    op.append(line[i])
                elif line[i]=="+":
                    while len(op)!=0 and (op[-1]=="*" or op[-1]=="+"):
                        first=stack.pop()
                        second=stack.pop()
                        op1=op.pop()
                        stack.append(mathOperation(first,second,op1))
                    op.append(line[i])
                elif line[i]=="/" or line[i]=="-":
                    raise TypeError("Invalid operator in Input")
                i+=1
            '''If stack still containing digits and operators then looping through stack and performing math operation.'''
            '''when stack is left with one.'''
            if len(stack)!=0 and len(op)!=0:
                first=stack.pop()
                second=stack.pop()
                op1=op.pop()
                stack.append(mathOperation(first,second,op1))
                txt="The output of {} is {}"
                print(txt.format(filepath,stack[-1]))
            else:
                raise TypeError("Error in Input")


getInputFiles()
