import numpy as np

x = np.arange(8).reshape(2, 4)
sum_x = np.sum(np.square(x), 1)
dist = np.add( np.add(-2 * np.dot(x, x.T), sum_x ).T, sum_x )

print(x)
print(sum_x)
print(dist)
