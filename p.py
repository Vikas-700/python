age1=int(input("Enter your date of birth year:"))
age2=int(input("Enter your date of birth month:"))
age3=int(input("Enter your date of birth date:"))
y=int(input("Enter today year:"))
m=int(input("Enter today month:"))
d=int(input("Enter today date:"))

y1=y-age1
if age2>m:
    y2=age2-m
    y1*=12
    y1-=y2
else:
    y2b=m-age2
    y1*=12
    y1+=y2b
if age3>d:
    y3=age3-d
    y1*=360
    y1-=y3
else:
    y3b=d-age3
    y3b*=360
    y1+=y3b  
y1/=360              
print("Your age",y1,"year")