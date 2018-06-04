def isArmstrong(n):
	n1 = n
	result = 0
	while(n1>0):
		rem = n1%10
		result += rem**3
		n1 = n1//10
	if(result == n):
		return True
	else:
		return False


for x in range(1,1000):
	if(isArmstrong(x)):
		print("%d is an armstrong number" %(x))
