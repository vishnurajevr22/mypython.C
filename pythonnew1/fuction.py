"""def newfunction(name,age,location):
    return f"i am{name}and {age} years old.my {location}"
print(newfunction(name="ragu",age=20,location="cdm"))
print(newfunction("vino",34,"myl"))

def oldfuction(name,*hobbies,**address):
    print("name=",name)
    print("hobbies=",hobbies)
    print("address=",address)
oldfuction("ram","cricket","vollybal",street ="11 new" , city="cdm")"""


#recursion


def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
         result =0
    return result
tri_recursion(7)


"""y=lambda a,b:a+b
print(y(6,7))"""

"""def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))"""

"""def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(9))"""

"""#example for arithmetic operation using conditionla statement
a=int(input("choose operation:"))
x=int(input("enter value:"))
            
b=int(input("enter value:"))
if a==1:
      print(x+b)
      if a==3:
          print(x*b)
          if a==4:
              print(a/b)
    
elif a==2:
    print(x-b)

else:
    print(none)"""


"""def prime(n):
      return n%n==0 and n%1==0 and n%2!=0 and n%3!=0

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(list(filter(prime,a)))



def even(n):
      return n%2==0
a=[1,2,3,4,5]
print(list(map(even,a)))"""














