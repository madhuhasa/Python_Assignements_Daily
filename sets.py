A = {5,3,8,6,1}
B = {1,5,3,4,2}

uni = A.union(B)
inter = A.intersection(B)
diff = A-B
maxA = max(A)
minA = min(A)
maxB = max(B)
minB = min(B)

print("union = " + str(uni))
print("intersection = "+ str(inter))
print("set difference = "+ str(diff))
print("max and min of set A = "+ str(maxA)+" and "+str(minA))
print("max and min of set B = "+ str(maxB)+" and "+str(minB))