import numpy as np 

my_list =[1,2,3,4,5]
my_array = np.array(my_list)
print("my list : ",my_list)
print("my array : ",my_array)
print("first element : ",my_array[0])
print("last element : ",my_array[4])
print("last element : ",my_array[-1])
multiplied_array =my_array*2
print("after doubling each element : ",multiplied_array)
zero_array = np.zeros(10)
print("an array of 10 zeros : ",zero_array)
one_array = np.ones(10)
print("an array of 10 ones : ",one_array)
five_array = np.full(10,5)
print("an array of 10 fives : ",five_array)
# write a numpy program to create a 3*3 matrix with valus ranging from 2 to 10 

#matrix = np.random.randint(0, 11, size=(3, 3))
matrix = np.arange(2,11).reshape(3,3)
print(matrix)