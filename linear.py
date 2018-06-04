import numpy as np
import matplotlib.pyplot as plt


def find_coeffs(x,y):
	mean_x = sum(x)/len(x)
	mean_y = sum(y)/len(y)
	numerator = 0
	denominator = 0
	for _ in range(len(x)):
		numerator += (x[_]-mean_x)*(y[_]-mean_y)
		denominator += (x[_]-mean_x)**2
	
	b2 = numerator/denominator
	b1 = mean_y - b2*mean_x
	y_calc = []
	for i in range(len(x)):
		y_calc.append((b1+b2*x[i]))
	
	print("Mean of x is " + str(mean_x))
	print("Mean of y is "+ str(mean_y))
	print("slope of line is " + str(b2))
	print("Y-intercept of the line is "+ str(b1))
	plt.plot(x,y,'ro')
	plt.plot(x,y_calc)
	plt.show()
	
	
	

	
x = [8,2,11,6,5,4,12,9,6,1]
y = [3,10,3,6,8,12,1,4,9,14]
find_coeffs(x,y)
