from random import randint


l="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*)("

pass_length=int(input("Enter the length of password : "))

print("Press 1 for level 1 complexity (only small letters)")
print("Press 2 for level 2 complexity (may include small letters and capital letters)")
print("Press 3 for level 3 complexity (may include letters and numbers too)")
print("Press 4 for level 4 complexity (may include letters numbers and special characters too)")
complexity=int(input("Enter the complexity : "))


password=""

if complexity==1:
    for i in range(0, pass_length):
        password += l[randint(0,25)]
elif complexity==2:
    for i in range(0, pass_length):
        password += l[randint(0,51)]
elif complexity==3:
    for i in range(0, pass_length):
        password += l[randint(0,61)]
elif complexity==4:
    for i in range(0, pass_length):
        password += l[randint(0,71)]
else:
    print("Invalid complextiy please choose from 1,2,3,4.")



print("The generated password : ",password)




