print("1.  Add")
print("2.  Subtract")
print("3.  Multiply")
print("4.  Divide")
option=int(input("Choose an Operation:- "))

a=float(input("enter ur first number:- "))
b=float(input("enter ur second number:- "))

if (option in [1,2,3,4]):
    
    if option==1:
        result = a+b

    elif option==2:
        result = a-b
        
    elif option==3:
        result=a*b
        
    elif option==4:
        if b!=0 :
            result=a/b  
        else:
            print("not divisible by zero")
            result= None
        
else:
    print("invalid operation")
    result= None

if result is not None:
    print(f"ur result is {result}")