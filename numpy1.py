import numpy as np

x = np.random.random()
print("random number: ", x)
x_squre_root = np.sqrt(x)
print("number square root: ", x_squre_root)
print("x^square(x)", np.power(x, x_squre_root))
matrix = np.random.random(3)
print("Random matrix: ", matrix)
matrix = np.append(matrix, np.random.random(2))
print("New matrix: ", matrix)
print("sine of matrix: ", np.sin(matrix))