try:
    a=int(input("enter the value"))
    b=int(input("enter the value"))
    c=a/b
    print(f"result:{c}")
except ZeroDivisionError as e:
    print("zero is not divisible")
finally:
    print("prgram is executed successfully")
