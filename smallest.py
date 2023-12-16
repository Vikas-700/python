num1=int (input("Enter First Value:"))
num2=int (input("Enter Second Value:"))
num3=int (input("Enter Third Value:"))
if num1<num2:
    if num1<num3:
        print("Frist Value Is Smallest:-",num1)
    else:
        print("Third Value Is Smallest:-",num3)    
elif num2<num3:
    print("Second Value Is Smallest:-",num2)
else:
    print("Trird Value Is Smallest:-",num3)    