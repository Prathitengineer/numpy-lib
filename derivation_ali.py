import numpy as np

A = np.array([[1,2],[3,4]])
print("A Matrix")
print(A)
print("standard deviation = ",np.std(A))
print("standard deviation of rows = ",np.std(A, axis = 0))
print("Standard deviation of columns = ",np.std(A, axis =1))
