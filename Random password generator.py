import random as r
def pswd_generator(a,b,c,d):
    password=''
    for i in range(2):
        password += r.choice(a)
        password += r.choice(b)
        password += r.choice(c)
        password += r.choice(d)
    print("\n",password)
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b='0123456789'
c='abcdefghijklmnopqrstuvwxyz'
d='!@#$%&*~'
pswd_generator(a,b,c,d)



