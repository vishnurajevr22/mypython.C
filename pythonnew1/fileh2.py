#file=open("example2.txt","x")

file=open("example2.txt","w+")
n=int(input("enter no person:"))
file.write("name \t age \t phno \t\t email \n")
for i in range(n):
    
    a=str(input("enter your name:"))
    b=int(input("enter age:"))
    c=int(input("enter ph no:"))
    d=input("enter email:")
    
    file.write(f"{a} \t {b} \t {c} \t {d}\n")
    

print("added content")
file.seek(0)
g=file.read()
print(g)
file.close()

