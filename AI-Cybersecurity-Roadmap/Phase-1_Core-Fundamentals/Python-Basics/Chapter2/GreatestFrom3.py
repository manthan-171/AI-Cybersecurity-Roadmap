a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
c = int(input("Enter value of c"))

if( a > b and a > c):
    print("A is greater")
elif(b > a and b > c):
    print("B is greater")
else:
    print("C is greater")