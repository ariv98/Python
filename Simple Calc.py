def opt():
    print("\nSelect option: \n")
    print('''\t1.Add 
    \t2.Subtract 
    \t3.Multiplication 
    \t4.Division
    \t5.All
    \t6.Exit \n ''')
    option=int(input("Your option: "))
    if option==1:
        add()
    elif option==2:
        print("Enter the two numbers: ")
        sub()
    elif option==3:
        mul()
    elif option==4:
        div()
    elif option==5:
        alll()
    elif option==6:
        print("\tBye bye")
    else:
        print("Please select correct option only: ( '1' '2' '3' '4' or '5' )")
        opt()

def choice():
    ch=input("Do you want to do another option (y/n): ")
    if ch=='y':
        opt()
    elif ch=='n':
        print("\n\t\tThankyou")
    else:
        print("Please select correct choice: ('y' or 'n' only)")
        choice()

def add():
    a=list(map(int,input("Enter the numbers: ").split()))
    b=sum(a)
    print(f'Your answer is: {b}')
    choice()

def sub():
    n1=int(input("1st number: "))
    n2=int(input("2nd number: "))
    print(f'Your answer is: {n1-n2}')
    choice()

def mul():
    b=1
    a=list(map(int,input("Enter the numbers: ").split()))
    for i in a:
        b*=i
    print(f'Your answer is: {b}')
    choice()

def div():
    n1=int(input("Divident: "))
    n2=int(input("Divider: "))
    print(f'Your answer is: {n1/n2}')
    choice()

def alll():
    a=input("Enter your problem ( Eg: 1+5*10-3/4 ): ")
    print(f'Your answer is: {eval(a)}')
    choice()

opt()



'''The below code is same as the above one,,,Don't get shocked'''

'''a=input("Enter your problem ( Eg: 1+5*10-3/4 ): ")
   print(eval(a))'''

'''LOL'''