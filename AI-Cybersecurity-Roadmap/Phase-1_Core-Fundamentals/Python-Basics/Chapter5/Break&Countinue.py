#Break
count = 1

while count <= 5:
    print(count)
    if (count == 2):
        break
    count += 1

tuple = (1,4,9,16,25,36,49,64,81,100)

index = 0

while index < len(tuple):
    if(tuple[index] == 64):
        print("Element At index", index)
        break
    else:
        print("Finding")
    index += 1

#Continue To print odd numbers
i = 1
while i <= 10:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1

#Countinue to print even numbers
i = 1 
while i <= 10:
    if(i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1