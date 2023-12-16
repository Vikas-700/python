import re
import random
coding = True
a=input(" Enter Any Message:")
a=re.split("\s",a)
new_mess=a[1:]
print(new_mess)
new_mess.append(a[0])
print(new_mess)
new_mess.reverse()
print(new_mess)
a=str(new_mess)
print(a)
x=re.sub("\s","7",a)
print(x)