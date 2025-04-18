list = ["Manthan",17,98.6,"Patel"]
print(list)
print(len(list))

print(list[0])
print(list[3])

list[1] = 19 #Allowed In List Not Allowed In String
print(list)


#List Slicing 
list1 = ["Hello" , 190 , 56.3 , "Moon"]
print(list1[0:2])
print(list1[:3])
print(list1[0:])

#List Methods
list3 = [82,3293,503,234,656,765]

print(list3.append(17))
print(list3)

print(list3.remove(3293))
print(list3)

print(list3.insert(1,41))
print(list3)

print(list3.sort())
print(list3)

print(list3.sort(reverse=True))
print(list3)

print(list3.reverse())
print(list3)    