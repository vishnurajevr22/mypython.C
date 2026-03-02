"""a=input("enter the value:")
if a.isupper():
    print(a.lower())
elif a.isdigit():
    print("numeric")

else:
    print(a.upper())"""

"""if True:
    print("1")
else:
    print("0")"""


"""if True:
    print("1")
    if False:
        print("0")
    else:
        print("2")
else:
    print("3")"""

"""a=int(input("enter your mark:"))
if a>=35:
    print("pass")
    if a>=85 and a<=100:
        print("grade A")
    elif a>=60 and a<85:
        print("grade B")
    elif a>=50 and a<60:
        print("grade C")
    elif a>=45 and a<50:
        print("grade d")
    elif a>=35 and a<50:
        print("grade e ")
    
else:
    print("fail")"""

a=int(input("enter your mark in 1:"))
b=int(input("enter your mark in 2:"))
c=int(input("enter your mark in 3:"))
d=int(input("enter your mark in 4:"))
e=int(input("enter your mark in 5:"))

g=((a+b+c+d+e)/500)*100
f=int(g)
print(f)

if f<50 and f>=35:
    print(" eligible for polytechnic")
    print("1.sss plytechnic college")
    print("2.bbb polytechnic college")
    print("3.aaa polytecn=hnic college")
elif f>50 and f<=75:
    print(" eligible for arts and science")
    print("1.eee arts and science college")
    print("2.bbb arts and science  college")
    print("3.aaa arts and science college")
elif f>75 and f<=100:
    print(" eligible for engineering")
    print("1.fff engineering college")
    print("2.iii engineering  college")
    print("3.jjj engineering college")
    

    




       
