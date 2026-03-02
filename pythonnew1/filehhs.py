"""#file=open("newfff.txt","x")
file=open("newfff.txt","w+")
file.seek(5)
file.write("hello everyone")
print("added")
file.seek()
g=file.read()
print(g)
file.close()"""


#file=open("user.txt","x")
#file=open("admin.txt","x")

a={"ram":2345,"joe":4556,"raja":9876}
b={"dece":6754,"there":7654,"you":4098}

print("""login as
1.admin
2.user""")
n=int(input("choice 1 or 2:"))

if n==1:
    name=input("enter adminname")
    
    if name in a:
        passwd=int(input("enter passwd"))
        if passwd==a[name]:
            print("login sucessfull")
            a=input("enter name")
            b=int(input("enter age"))
            c=int(input("enter phno"))
            d=input("enter email")
            file=open("admin.txt","w+")
            file.write(f"name={a}\n")
            file.write(f"age={b}\n")
            file.write(f"phno={c}\n")
            file.write(f"email={d}\n")
            file.close()
        else:
            print("incorrect passwd")
    elif name in b:
        print("you are user choose 2")
    else:
        print("adminname is incorrect")
        
                

elif n==2:
    name=input("enter username")
    
    if name in b:
        passwd=int(input("enter passwd"))
        if passwd==b[name]:
            print("login as user")
            a=input("enter name")
            b=int(input("enter reg no"))
            c=int(input("enter year"))
            d=input("enter depmt")
            file=open("user.txt","w+")
            file.write(f"name={a}\n")
            file.write(f"reg no={b}\n")
            file.write(f"year={c}\n")
            file.write(f"depmt={d}\n")
            file.close()
        else:
            print("incorrect passwd")
    elif name in a:
        print("you are admin choose 1")
    else:
        print("username is incorrect")
            
    
else:
    print("invalid")

    
