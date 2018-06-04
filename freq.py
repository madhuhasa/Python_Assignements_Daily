import numpy as np
import matplotlib.pyplot as plt
from statistics import mode


def print_mean_mode_median(data,size):
	mean = sum(data)/size
	mod = mode(data)
	if size%2!=0:
		median = data[size//2]  
	else:
		median = (data[size//2]+data[size//2+1])/2

	print("mean is "+ str(mean))
	print("mode is "+ str(mod))
	print("median is "+ str(median))


def generateFreqDist(data):
		intervals = ["421-440","441-460","461-480","481-500","501-520","521-540","541-560","561-580","581-600","601-620"]
		counts = {}
		for i in range(len(data)):
			for j in range(len(intervals)):
				low,high = map(lambda x: int(x),intervals[j].split("-"))
				if(data[i]>=low and data[i]<=high):
						if((low,high) not in counts):
							counts[(low,high)] = 1
							break
						else:
							counts[(low,high)] += 1
							break

		print("Intervals    Frequency")
		freq = []
		for x,y in counts.items():
			freq.append(y)
			print('{}     {}'.format(x,y))
		
		cum_freq = np.cumsum(freq)
		print(cum_freq)
		
		plt.bar(intervals,freq)
		line1, = plt.plot(intervals, cum_freq,'bo',label="Cumulative Freq Dist")
		plt.plot(intervals, cum_freq,'k')
		plt.xlabel("Intervals")
		plt.ylabel("Frequency")
		plt.legend(handles = [line1],loc = 0)
		plt.show()
		
		
		

	
	
data = []
fo = open("data.txt","r")


for line in fo.readlines():
	x = line.split(",")
	for _ in range(len(x)):
		data.append(int(x[_]))
		
	
data = sorted(data)
size = len(data)
print_mean_mode_median(data,size)
print("Standard Deviation = " + str(np.std(data)))
coeff_var = np.std(data)/mean * 100
print("Coefficient of Variance = "+ str(coeff_var))
generateFreqDist(data)

