a=float(input("Enter first number : "))
b=float(input("Enter second number : "))

print(f"Press 1 to perform addition operation when {a} is added to {b}  (+)")
print(f"Press 2 to perform addition subtraction when {a} is subtracted by {b}  (-)")
print(f"Press 3 to perform addition multiplication when {a} is multiplied by {b}  (*)")
print(f"Press 4 to perform addition division when {a} is divided by {b} (/)")
print(f"Press 5 to perform floor division when {a} is divided by {b}  (//)")
print(f"Press 6 to perform find remainder when {a} is divided by {b} (%)")

choice=int(input("Enter your choice here : "))

if choice==1:
    print("The answer is : ",a+b)
elif choice==2:
    print("The answer is : ",a-b)
elif choice==3:
    print("The answer is : ",a*b)
elif choice==2:
    print("The answer is : ",a/b)
elif choice==2:
    print("The answer is : ",a//b)
elif choice==2:
    print("The answer is : ",a%b)
