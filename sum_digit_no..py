n = int(input("Enter the number"))
temp =0

while(n>0):
    dog = n % 10
    temp = temp + dog
    n = n//10
print("The total is :",temp )
    