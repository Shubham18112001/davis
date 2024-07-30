# Task 1: Find the mean of each NumPy array in the list

import numpy as np

list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]

means = [np.mean(arr) for arr in list]
print("Mean of Each array:", means)
