a=input("Enter infinite times 1=")   
str(sum)=0
str(i)=1
while(a>=i):
    series=i+i
    if series>a:
        break
    sum+=series    
print("sum of series=",sum)          