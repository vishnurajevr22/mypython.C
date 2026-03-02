#file=open("sample.txt","x")

"""file=open("sample.txt","w")
file.write("hello,world")
file.close()
print("file is created")"""


"""file=open("sample.txt","a")
file.write("this is new line in file")
file.close()
print("successfully")"""


"""file=open("sample.txt","r")
content=file.read()
print(content)"""

'''file=open("sample.txt","wb")
file.write(b"helo world")
file.close()
print("succ")'''


"""file=open("sample.txt","rb")
content=file.read()
print(content)"""


"""file=open("sample.txt","wb")
file.write(b"hello world")
file.close()
print("cnotent added")"""

"""file=open("sample.txt","rb")
c=file.read()
print(c)"""

f"""ile=open("sample.txt","rb")
d=file.read()
print(d.decode())"""

"""file=open("sample.txt","wb")
d="hello"
file.write(d.encode())

file=open("sample.txt","rb")
d=file.read()
print(d.decode())"""
#seek
file=open("sample.txt","r+")


#file.write("this is new content added ")
#print("added")
"""file.seek(8)
d=file.read()
print(d)"""
file.seek(0)
d=file.readline()
print(d)


































