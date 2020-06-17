# modules in python is a file (eg as sections in supermarket)
#we refer to each file as a module

import converters

print(converters.kg_to_lbs(90))
print(converters.lbs_to_kg(150))

from utils import find_max

numbers=[1,4,5,8,10]
max=find_max(numbers)
print(max)