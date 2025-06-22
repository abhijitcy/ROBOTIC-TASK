import numpy as np

a=np.array([[45,60] ,[30,80]])
a[a>50] =100

columnMean =np.mean(a,axis=0)

print("THE ARRAY:" ,a)
print("\nColumn-wise Means :\n" ,columnMean)
