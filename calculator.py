a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
op=input("Enter operator (+,-,*,/,%,**):")

if op=='+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='%':
    print(a%b)
elif op=='**':
    print(a**b)
else:
    print("Invalid argument")