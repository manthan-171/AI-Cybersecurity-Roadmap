abc = {1,42,56,"hellow" , 32.13}
print(type(abc))

#To Make Empty Set
new_set  = set()
print(new_set)

#Set Methods

#Add Element In Set
abc.add(222)
print(abc)

#Remove Element From Set 
abc.remove(222)
print(abc)

#Remove Random Element From Set
abc.pop()
print(abc)

#Clear The Set
abc.clear()
print(abc)

# Union & InterSection In A set
set1 = {1,3,4,2,7}
set2 = {1,2,5,9,10,7}

print(set1.union(set2))
print(set1.intersection(set2))
