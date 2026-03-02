#file=open("example.txt","x")

file=open("example.txt","w+")
n=int(input("enter no person:"))
for i in range(n):
    
    a=str(input("enter your name:"))
    b=int(input("enter age:"))
    c=int(input("enter ph no:"))
    d=input("enter email:")
    file.write(f"name={a}\n")
    file.write(f"age={b}\n")
    file.write(f"ph no={c}\n")
    file.write(f"email={d}\n")
    file.write("\n")
    



print("added content")
file.seek(0)
g=file.read()
print(g)
file.close()



