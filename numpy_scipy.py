import numpy as np
a = np.array((2,2))
print(a)
b = np.ones((1,2))
print(b)
c = np.full((2,2), 7, np.float32)
# c = np.full((2,2), 7, np.double)
print(c)
d = np.eye(2)
print(d)
e = np.random.random((2,2))
print(e)
f = np.array([[1,2,3,4],[11,22,33,44],[111,222,333,444]])
print(f)