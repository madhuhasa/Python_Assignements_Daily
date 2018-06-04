def factorial(n):
	if n==0:
		return 1
	if n==1:
		return 1
	else:
		fact = 1
		for i in range(2,n+1):
			fact = fact*i
		
		return fact

		
def HCF(a,b):
	while(a!=0 and b!=0):
		if(a>b):
			a = a-b
		else:
			b = b-a
	
	ans = a if a!=0 else b
	return ans
	

def LCM(a,b):
	gcd = HCF(a,b)
	lcm = a*b // gcd
	return lcm

	
def findFactors(number):
	factors = [1]
	factors.append(number)
	for x in range(2,number//2):
		if number % x ==0:
			if(x  not in factors):
				factors.append(x)
				y = number//x
				if(y not in factors):
					factors.append(y)
	
	return factors
			

while(1):
	print("Enter a number - ")
	print("FACTORIAL --> 1")
	print("LCM --> 2")
	print("HCF --> 3")
	print("FACTORS --> 4")
	print("EXIT--> 5")
	
	number  = int(input())
	if(number == 1):
		print("Enter a number for finding factorial")
		n = int(input())
		print("Factorial of %d is " %(n) + str(factorial(n)))
	
	elif(number == 2):
		print("Enter two numbers with space for finding LCM")
		x, y = map(lambda x: int(x),input().split(" "))
		print(LCM(x,y))
		
	elif(number == 3):
		print("Enter two numbers with space for finding HCF")
		x, y = map(lambda x: int(x),input().split(" "))
		print("HCF of %d and %d is - " %(x,y) + str(HCF(x,y)))
		
	elif(number == 4):
		print("Enter a number to find its factors-")
		n = int(input())
		fact = findFactors(n)
		print("Factors of %d are " %(n) + str(fact))
		
	elif(number == 5):
		print("Thank you for using the calculator")
		break
		
	else:
		print("Input not recognised. Enter a correct number")
		
