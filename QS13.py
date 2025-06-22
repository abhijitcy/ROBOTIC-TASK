import numpy as np
arr = np.random.randint(1, 101, size=(5, 5))

# Replace all even numbers with 0
arr[arr % 2 == 0] = 0


print(arr)
