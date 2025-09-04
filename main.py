import numpy as np

# Scalar arithetic

# array = np.array([1,2,3])

# print(array + 1)
# print(array - 1)
# print(array * 2)
# print(array / 2)

# # Elementwise arithetic

# array = np.array([1,2,3])
# print(array + array)
# print(array - array)
# print(array * array)
# print(array / array)

# # Vectorized math funcs

# array = np.array([1.01, 2.5, 3.99])
# print(np.sqrt(array))
# print(np.exp(array))
# print(np.log(array))
# print(np.round(array))
# print(np.ceil(array))
# print(np.floor(array))
# print(np.trunc(array))

# # Trigonometric funcs

# array = np.array([0, np.pi/2, np.pi])
# print(np.sin(array))
# print(np.cos(array))
# print(np.tan(array))

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])

# 2D array (matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Zeros, Ones, and Random
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
randoms = np.random.rand(3, 3)
print(zeros)
# print(ones)
# print(randoms)

scores = np.array([65, 70, 88, 92, 78, 85, 90, 76, 60])

mean = np.mean(scores)
std_dev = np.std(scores)
above_avg = scores[scores > mean]

print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Scores above average:", above_avg)


