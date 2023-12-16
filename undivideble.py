num1=int(input("Enter Any Number:"))
list1=[]
for i in range(num1,2,-1):
    x=2
    while True:
        if num1%x==0:
            if num1==x:
               list1.append(x)
               print(f"{num1} is Divideble by {x}")
            break
        else:
            x+=1
    num1-=1
list1.reverse()    
print(list1)