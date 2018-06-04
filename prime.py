import math

def Isprime(number):
	flag = 1
	for i in range(2,int(math.sqrt(number))):
		if(number%i==0):
			flag = 0
			break
	if flag==1:
		return True
	else:
		return False


def isPalindrome(number):
	rev = 0
	while(number>0):
		rem = number%10
		rev = rev*10+rem
		number = number//10
	
	if(number == rev):
		return True
	else:
		return False


lis = []
for x in range(900,1001):
	if (Isprime(x)):
		lis.append(x)

print(lis)

for x in lis:
	if(isPalindrome(x)):
		print("palidrome - "+ str(x))