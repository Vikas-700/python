marks1=input("Enter Hindi Marks")
while(float(marks1)>100.0):
    print("Warning You Are Enter Wrong Marks")  
    marks1=input("Re-Enter Hindi Marks")
    marks1=float(marks1)
marks2=input("Enter Art Marks")
while(float(marks2)>100.0):
    print("Warning You Are Enter Wrong Marks")
    marks2=input("Re-Enter Art Marks")
    marks2=float(marks2)
marks3=input("Enter Science Marks")
while(float(marks3)>100.0):
    print("Warning You Are Enter Wrong Marks")
    marks3=input("Re-Enter Science Marks")
    marks3=float(marks3)
marks4=input("Enter English Marks")
while(float(marks4)>100.0):
     print("Warning You Are Enter Wrong Marks")
     marks4=input("Re-Enter English Marks")
     marks4=float(marks4)
marks5=input("Enter Math Marks")
while(float(marks5)>100.0):
    print("Warning You Are Enter Wrong Marks")
    marks5=input("Re-Enter Math Marks")
    marks5=float(marks5)
marks=float(marks1)+float(marks2)+float(marks3)+float(marks4)+float(marks5)
per=float(marks)/5
print(per)
if(per>=33.0 and per<=50.0):
        print("You Are Pass With Grade C")
elif(per>50.0 and per<=70.0):
        print("You Are Pass With Grade B")
elif(per>70.0 and per<=100.0):
        print("You Are Pass With Grade A") 
else:
        print("Sorry! You Are Fail")           