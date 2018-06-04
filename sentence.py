import re

def palindrome(word):
	x = list(word)
	reverse = x[::-1]
	if x == reverse:
		return True
	else:
		return False
		
		

regexp = "[^A-Za-z0-9 ]"	 	
sentence = "#Python is an interpreted high level programming language for general-purpose programming*"
y = re.sub(regexp," ",sentence)
y = y.strip()
words = y.split(" ")
#print(words)
freq = {}
for word in words:
	if(palindrome(word)):
		print(word)
	if word in freq:
		freq[word] += 1
	else:
		freq[word] = 1

print("WORD-FREQUENCY")
for x,y in freq.items():
	print(x + "-" + str(y))
