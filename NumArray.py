
#create a numpy Array
#Arrays are created using the np.array() function
import numpy as np  # type: ignore[import-not-found]
array1 = np.array([1, 2, 3, 4, 5])
print(array1)

#two dimensional array from nested lists
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array2)

#one dimensional array from a tuple
array3 = np.array((7, 8, 9, 10))
print(array3)

#accessing elements in a numpy array
print(array1[0])  # prints the first element of array1
print(array2[0, 0])  # prints the first element of the first row of array2
print(array3[3])  # prints the fourth element of array3