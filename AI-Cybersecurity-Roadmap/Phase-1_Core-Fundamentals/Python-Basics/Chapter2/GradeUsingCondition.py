marks = float(input("Enter Marks"))

if(marks >= 90):
    print("GRADE A")
elif(marks >= 80 and marks < 90):
    print("GRADE B")
elif(marks >= 70 and marks < 80):
    print("GRADE C")
else:
    print("GRADE D")