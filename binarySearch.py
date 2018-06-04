def binarySearch(A,key):
	if(len(A)==0):
		return -1
	
	
	mid = len(A)//2
	if(A[mid]==key):
		return mid
	
	else:
		if key<A[mid]:
			return binarySearch(A[:mid],key)
		else:
			return binarySearch(A[mid+1:],key)

			
			


