# Task 3: Compute the standard deviation of the NumPy array

import numpy as np

arr = np.array([20, 2, 7, 1, 34])
print("arr : ", arr)
std_deviation = np.std(arr)
print("Standard deviation of arr:", std_deviation)

std_deviation_float32 = np.std(arr.astype(np.float32))
std_deviation_float64 = np.std(arr.astype(np.float64))

print("More precision with float32\nstd of arr:", std_deviation_float32)
print("More accuracy with float64\nstd of arr:", std_deviation_float64)