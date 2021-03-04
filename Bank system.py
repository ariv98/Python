db = {}

def initial():
    print("\n\t\tWELCOME TO ABC BANK\n")
    print("\n\tPlease select an option to proceed\n")
    print("1. LOGIN")
    print("2. SIGNUP")
    print("3. EXIT")
    print("4. ADMIN")
    a=input("\nEnter choice: ")
    if a=='1':
        login()
    elif a=='2':
        signup()
    elif a=='3':
        print("\nThanks for choosing ABC bank...come again")
        exitt()
    elif a=='4':
        print("\n\t\tADMIN USE")
        admin()
    else:
        print("\n\t\t!!!Choose correct option!!!")
        initial()

def initial2():
    print("\n\t\tChoose your need\n")
    print("1.BALANCE ENQUERY")
    print("2.WITHDRAW")
    print("3.LOGOUT")
    b=input("\nEnter choice: ")
    if b=='1':
        balance_enquery()
    elif b=='2':
        withdraw()
    elif b=='3':
        print("\t\tLOGOUT successful")
        initial()
    else:
        print("\n\t\t!!!Choose correct option!!!")
        initial2() 

def login():
    print("\n\t\tWelcome to LOGIN\n")
    uname=input("Enter username: ")
    if uname in db:
        pswd=input("Enter password: ")
        if pswd in db[uname]==pswd:
            print("Login successful")
            print(f'\n\t\tHello {uname.upper()} Welcome to ABC bank')
            initial2()
        else:
            print("\t\t!!!!!Wrong password!!!!!")
            print("Enter correct password")
            pswd=input("Enter password: ")
            if pswd in db[uname]==pswd:
                print("\n\t\tLogin successful!!!\n")
                print(f'\t\tHello {uname.upper()} Welcome to ABC bank')
                initial2()
            else:
                print("Sorry no more chance left...Try LOGIN again")
                initial()
    else:
        print("\t!!!Username does't exist goto SIGNUP or Enter correct username in LOGIN!!!")
        initial()

def signup():
    print("\n\t\tWelcome to SignUp\n")
    uname=input("Enter username: ")
    if uname in db:
        print("!!!Username already exist please try other name!!!")
        signup()
    else:
        print("Username created succefully!!!\n")
        pswd=input("Enter password: ")
        print("\n\t\tSignUp successful!!!")
        print("\t\tNow LOGIN to your account")
        db[uname]=pswd
        initial()

def exitt():
        print("\n\t\t!!!Goodbye!!!")

def balance_enquery():
    amt=1000
    print(f'Your current balance is Rs: {amt}')
    initial2()

def withdraw():
    print("\n\t\t WITHDRAW\n")
    amt=input("Enter the amount: ")
    print(f'Your amount Rs: {amt} has been withdrawn successfuly')
    initial2()

def admin_login():
    aname=input("Enter name: ").upper()
    if aname=='ARIVAZHAGAN':
        apswd=input("Enter password: ")
        if apswd=='ariv98':
            alogin()
        elif apswd!='ariv98':
            print("\n!!!Wrong password!!!")
            initial()
    elif aname!='ARIVAZHAGAN':
        print("\n!!!ADMIN name wrong...")
        initial()

def alogin():
    print("\n\t\tHello ADMIN")
    print("\n\t\tChoose your need\n")
    print("1. VIEW USERS")
    print("2. VIEW FULL DATABASE")
    print("3. LOGUT")
    d=input("\nEnter choice: ")
    print("\n")
    if d=='1':
        if len(db)==0:
            print("The DATABASE is EMPTY")
            alogin()
        else:
            for i in db:
                print(i)
            alogin()
    elif d=='2':
        if len(db)==0:
            print("The DATABASE is EMPTY")
            alogin()
        else:
            print("USERNAME      : PASSWORD")
            for i,j in db.items():
                print(f'{i}         : {j}')
            alogin()
    elif d=='3':
        print("\t\t\t\nLOGOUT successful")
        initial()
    else:
        print("\n\t\t!!!Choose correct option!!!")
        alogin()

def admin():
    print("\n\t\tChoose your need\n")
    print("1. LOGIN")
    print("2. Back to HOME")
    print("3. EXIT")
    c=input("\nEnter choice: ")
    if c=='1':
        admin_login()
    elif c=='2':
        initial()
    elif c=='3':
        exitt()
    else:
        print("\n\t\t!!!Choose correct option!!!")
        admin()

initial()