import numpy as np

mvalues = [0, 1, 5, 6, 80]
M = np.array(mvalues)
print("M = ", M)
print(M*39.3701)

x = np.arange(20, 104.75, 3.6)
print("x.arrange = ", x)
x = np.linspace(20, 104.75, 10, endpoint=False)
print("x.linspace = ", x)

# returning spacing,_ is beacouse we don't care about the actual array now
_, spacing = np.linspace(20, 104.75, 10, retstep=True)
print("Spacing between the items in array above: ", spacing)
x = np.array([1, 2, 3, 4,])
print("x array", x)
print("the type of x", type(x))
print("the dimension of the x: ", np.ndim(x))
