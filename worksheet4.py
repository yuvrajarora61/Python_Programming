import numpy as np

# # Ques 1:

# arr1 = np.arange(5,26)
# print("1D array from 5 to 25:\n", arr1)

# arr2 = np.random.randint(10, 51, size=(3,4))
# print("\n2D array with random integers:\n", arr2)

# # ques2:

# print("\n1D Array Attributes:")
# print("Shape:",arr1.shape)
# print("Size:",arr1.size)
# print("Data Type:",arr1.dtype)


# print("\n2D Array Attributes:")
# print("Shape:",arr2.shape)
# print("Size:",arr2.size)
# print("Data Type:",arr2.dtype)

# #ques3:
# array1 = np.array([2,4,6,8,10])
# array2 = np.array([1,3,5,7,9])
# print("Addition:", array1+array2)
# print("Element-wise Multiplication:", array1*array2)
# print("Element-wise division:", array1/array2)


# # ques4:

# arr = np.arange(1,10).reshape(3,3)
# print("Original 2D array:\n", arr)
# result = arr*5
# print("\nAfter Broadcasting (multiplying with 5):\n",result)


# # ques5:

# arr = np.arange(10,26).reshape(4,4)
# print("Original Array\n", arr)

# second_row = arr[1,:]
# last_column = arr[:,1]
# print("\nScond Row:", second_row)
# print("Lat column:", last_column)

# arr[0,:] = 0
# print("\nArray after replacing first row with zeros:\n",arr)


# # ques6:

# arr = np.random.randint(20,41,size=10)
# print("Original Array:", arr)

# greater_than_30 = arr[arr>30]
# print("Elements greater than 30:", greater_than_30)


# #ques7:

# arr = np.arange(11,23)
# print("Original array:\n",arr)

# reshaped_arr = arr.reshape(3,4)
# print("\nReshaped 2D array(3x4):\n",reshaped_arr)


# #ques8:

# A = np.array([[1,2],[3,4]])
# B = np.array([[5,6],[7,8]])
# print(A)
# print(B)
# # matrix_mul = np.dot(A,B)
# matrix_mul = A @ B
# print("Matrix multiplication:\n", matrix_mul)

# transpose_A = A.T
# print("\nTranspose Of Matrix:\n",transpose_A)


# # ques9:

# arr = np.random.randint(10,61,size=15)
# print("Array:",arr)

# mean_val = np.mean(arr)
# median_val = np.median(arr)
# std_dev = np.std(arr)

# print("\nMean:",mean_val)
# print("Median:",median_val)
# print("Standard Deviation:",std_dev)


# # ques10:

# A = np.array([[2,1,3],[0,5,6],[7,8,9]],dtype=float)

# det_A = np.linalg.det(A)
# inv_A = np.linalg.inv(A)
# eigvals, eigvecs = np.linalg.eig(A)

# print("Matrix A:\n",A)
# print("\nDeterminent of A:\n",det_A)
# print("\nInverse of A:\n",inv_A)
# print("\nEigenvalues of A:\n",eigvals)
# print("\nEigenvectors of A(columns correspond to eigenvalues):\n",eigvecs)


# #Ques 11:

# path = np.array([[0,0],[2,3],[4,7],[7,10],[10,15]])


# dist = np.linalg.norm(path[-1] - path[0])
# print("Distance Between First and Last Point:",dist)


# diffs = np.diff(path, axis=0)
# dists = np.sqrt(np.sum(diffs**2, axis=1))
# total = np.sum(dists)
# print(total)





