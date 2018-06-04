import numpy as np

n_rows = 3
n_cols = 4

A = []
for x in range(n_rows):
	B = []
	for y in range(n_cols):
		B.append(int(input()))
	A.append(B)

A = np.array(A)
print(np.shape(A))

#Original Array reshaped to 3d array

array_3d = A.reshape(2,3,2)
print("Original Array reshaped to 3d array:")
print(array_3d)

print("Adding 5 to every element")
print(array_3d + 5)
print("Subtracting 2 from every element")
print(array_3d - 2)
print("Multiplying 5 to every element")
print(array_3d * 5)
