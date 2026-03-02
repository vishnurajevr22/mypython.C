def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


def tri_recurtion(k):
    if(k>0):
        result=k+tri_recurtion(k-1)
    else:
        result=0
    return result

def reverse(a,b=0):
    while a>0:
        c=a%10
        b=b*10+c
        a//=10
    return b

