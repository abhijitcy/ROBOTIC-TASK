import numpy as np

# Create two 3x3 
arr1 = np.random.randint(1, 11, size=(3, 3))
arr2 = np.random.randint(1, 11, size=(3, 3))
result = arr1 == arr2
print("Array 1:\n", arr1)
print("Array 2:\n", arr2)
print("Element-wise equality:\n", result)
