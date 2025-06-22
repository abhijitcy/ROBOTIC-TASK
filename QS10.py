def removeMid(I):

 n = len(I)

mid n // 2

 if n % 2 == 0:



return I[:mid-1] +

I[mid+1:] 

 else:



return I[:mid] +

I[mid+1:] 




I = [10, 20, 30, 40, 50]

 print(removeMid(1))



 p = [ 20, 30 60 70]

 print(removeMid(p))
