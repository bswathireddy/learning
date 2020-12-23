'''imported os to get input files using os.listdir.'''
'''imported re  becuase i used reg expression to match withe the input lines.'''
'''Collections because used deque to solve p8. '''
import os
import re
import collections
'''Defined a Method to get all input files which starts with t8 and endswith .dat.'''
'''Handling Errors using try and except.'''
'''Big O notation for this Function is O(n).'''
def getinputFiles():
    for file in os.listdir("."):
        m = re.match("^t8.*\.dat$", file.rstrip())
        if m:
            try:
                if os.path.getsize(file)==None:
                    raise TypeError("File is Empty")
                else:
                    print(file,":")
                    shelterAnimals(file)
            except Exception as err:
                print("Error: ",file,err)
            finally:
                print("==================")
'''Initialized deque for both dogs and cats separately to store dogs and cats respectively along with an order number.'''
dogs=collections.deque([])
cats=collections.deque([])
order=0
'''Defined Function Method called shelterAnimals to readfiles and put animals into shelter and dequeueing animals as well.'''
'''Big O Notation for this is O(n).'''
def shelterAnimals(filepath):
    with open(filepath) as f:
        global dogs,cats,order
        dogs = collections.deque([])
        cats = collections.deque([])
        order = 0
        for line in f.readlines():
            if line.strip()=="":
                continue
            match1=re.match(r'^[\s]*([a-zA-Z]+)[\s]*\([\s]*([a-zA-Z,\s]*)[\s]*\)',line)
            if match1:
                queue=match1.group(1)
                if queue=='enqueue':
                    params=match1.group(2).split(",")
                    type=params[0].strip()
                    name=params[1].strip()
                    enqueue(type,name)
                elif queue=='dequeue':
                    type=match1.group(2).strip()
                    if type == "dog":
                        dequeueDog(type)
                    elif type == "cat":
                        dequeueCat(type)
                    else:
                        print("Invalid Animal")
                elif queue=='dequeueAny':
                    if match1.group(2).strip()!="":
                        print("dequeueAny can't have parameters")
                    else:
                        dequeueAny()
                else:
                    print("Invalid Method")
            else:
                print("Invalid format")
'''Enqueue function Method to put the animal into shelter.'''
'''Big O Notation is O(1).'''
def enqueue(pettype,petname):
    if pettype=='dog':
        global order
        dogs.append((petname,order))
        print("put the dog named "+petname+" to the shelter.")
        order= order+1
    elif pettype=='cat':
        cats.append((petname,order))
        print("put the cat named "+petname+" to the shelter.")
        order=order+1
    else:
        print("Invalid Animal")
'''Function Method for deque dog.'''
'''Big O Notation is O(1).'''
def dequeueDog(pettype):
    if dogs:
        dog=dogs.popleft()
        print("the dog named "+dog[0]+" is adopted.")
    else:
        print("No dog left to be adopted.")
'''Function Method for deque cat.'''
'''Big O Notation is O(1).'''
def dequeueCat(pettype):
    if cats:
        cat=cats.popleft()
        print("the cat named "+cat[0]+" is adopted.")
    else:
        print("No cat left to be adopted.")
'''DequeueAny is a method where as both either cat or dog to dequeue.'''
'''Big O Notation is O(1).'''
def dequeueAny():
    if not dogs and not cats:
        print("No animal to adopt")
    elif not dogs:
        cat=cats.popleft()
        print("the cat named "+cat[0]+" is adopted.")
    elif not cats:
        dog=dogs.popleft()
        print("the dog named "+dog[0]+" is adopted.")
    else:
        dog=dogs[0]
        cat=cats[0]
        if dog[1]>cat[1]:
            cats.popleft()
            print("the cat named " + cat[0] + " is adopted.")
        else:
            dogs.popleft()
            print("the dog named " + dog[0] + " is adopted.")


getinputFiles()
'''As required all my OPERATIONS are in O(1) and getting inputfiles and reading files is in O(n).'''
'''Used timeit and checked time in jupyter, so my execution time for p8 is 2.35 ms ± 237 µs per loop (mean ± std. dev. of 7 runs, 100 loops each).'''