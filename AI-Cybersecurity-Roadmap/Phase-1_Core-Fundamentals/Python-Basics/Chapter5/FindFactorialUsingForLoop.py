#using For loop
n = 5
fact = 1

for i in range(1,n+1):  
    fact *= i
print(fact)

#using While Loop
n = 5
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1
print(fact)