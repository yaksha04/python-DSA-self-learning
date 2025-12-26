a=int(input("enter a:"))
b=int(input("enter b:"))
op=input("enter operator: ")
if op=='+':
    print( a + b)
elif op=='*':
    print(a * b)     
elif op == '-':
    print(a-b)    
elif op=='/':
    if b!=0:
        print(a/b)
    else:
        print(" write correct num 'b' ")
else:
    print("invalid operator")                