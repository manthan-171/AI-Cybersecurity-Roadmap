list = [1,4,9,16,25,36,49,64,81,100]

for i in list:
    print(i)
print("End of loop")

tuple = (1,4,9,16,25,36,49,64,81,100)

index = 0

for j in tuple:
    if(j == 9):
        print("Fount at" , index)
    index += 1
print("End of loop")
