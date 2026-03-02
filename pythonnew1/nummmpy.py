import numpy as np

arr1=np.array([1,2,3,4,5,6])
arr2=np.array([[3,4,5],[6,7,8]])
arr3=np.array([3,4,5,6,7,8,9])
zeros=np.zeros((4,4))
ones=np.ones((2,2))
ident=np.eye(4)
rando=np.random.rand(3,3)

"""print(arr1)
print(arr2)
print(arr3)
print(zeros)
print(ones)
print(ident)
print(rando)"""

print("shape:",arr2.shape)
print("size:",arr2.size)
print("datatype:",arr2.dtype)
print("dimensions:",arr2.ndim)


