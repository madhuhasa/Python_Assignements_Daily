import numpy as np


a = ([['Rhia',10,20,30,40,50],['Alan',75,80,75,85,100],['Smith',80,80,80,90,95]])

A = np.array(a)

slice_A = A[:,0:2]
print("--- Matrix after slicing ---")
print(slice_A)
A[2] = ['Sam',82,79,88,97,99]
print("Updated Matrix --")
print(A)
A[1][4] = 95
new_col = [[73],[80],[85]]
np.append(A,new_col,axis = 1)
print("Matrix after appending new column--")
print(A)