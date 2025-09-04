import numpy as np

# Scalar arithetic

array = np.array([1,2,3])

print(array + 1)
print(array - 1)
print(array * 2)
print(array / 2)

# Elementwise arithetic

array = np.array([1,2,3])
print(array + array)
print(array - array)
print(array * array)
print(array / array)

# Vectorized math funcs

array = np.array([1.01, 2.5, 3.99])
print(np.sqrt(array))
print(np.exp(array))
print(np.log(array))
print(np.round(array))
print(np.ceil(array))
print(np.floor(array))
print(np.trunc(array))

# Trigonometric funcs

array = np.array([0, np.pi/2, np.pi])
print(np.sin(array))
print(np.cos(array))
print(np.tan(array))


