def kthSmallest(A, B, k):
	mergedList= []
	i=0; j=0; count = 0
	m = len(A)
	n = len(B)
	while i < m and j < n and count < k:
		count += 1
		if(A[i]<B[j]):		
			if count == k:
				return A[i]
			i+=1					
		else:
			if count == k:
				return B[j]
			j+=1

	if(i<m):
		return A[i+k-count-1]
	if(j<n):
		return B[j+k-count-1]
	
	if k < len(mergedList):
		return mergedList[k-1] 
	else:
		return None
	
A = [1, 5, 8, 10, 50]
B = [3, 4, 29, 41, 45, 49, 79, 89]
print kthSmallest(A, B, 13)
print kthSmallest(A, B, 5)
print kthSmallest(A, B, 1)
