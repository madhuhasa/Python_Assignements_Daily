try:
	n = int(input())
	d = {}
	for i in range(n):
		d[i] = i*i

	print(d)
	
except ValueError:
	print("Non-numeric data entered. Please enter a number")