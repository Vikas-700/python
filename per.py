subject1=int(input("Enter Math Marks(1-100):"))
while subject1>100:
    print("This is wrong marks:")
    subject1=int(input("Enter Math Marks(1-100):"))
subject2=int(input("Enter Sanskrit Number(1-100):"))
while subject2>100:
    print("This is wrong marks:")
    subject2=int(input("Enter Sanskrit Marks(1-100):"))
subject3=int(input("Enter Enlish Marks(1-100):"))
while subject3>100:
    print("This is wrog marks:")
    subject3=int(input("Enter Enlish Marks(1-100):"))
subject4=int(input("Enter Science Marks(1-100):"))
while subject4>100:
    print("This is wrong marks:")
    subject4=int(input("Enter Science Marks(1-100):"))
sum=subject1+subject2+subject3+subject4
print("Total Marks=",sum)
per=(sum*100)/400
print("Percentage=",per,"%")
if per>=80:
    print("GRADE-A")
elif per<80 and per>60:
    print("GRADE-B")
elif per<60 and per>=50:
    print("GRADE-C")
else:
    print("FAIL")            










