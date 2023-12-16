x=int(input("Enter Any Number"))
for i in range(2,x+1):
    if x%i==0:
        if i==x:
             print(x,"Is a prime number")
        else:
            print(x,"Is not a prime Number")
            break