number=int(input(" number of term"))
star=1
sum=0
for i in range(0,number):
    print("series",star,end=" ")
    star=(star*10)+1
    sum=sum+star
print("total sum=",sum)    