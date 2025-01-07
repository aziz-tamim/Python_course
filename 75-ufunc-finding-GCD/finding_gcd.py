import numpy as np
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)


import numpy as np
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)
