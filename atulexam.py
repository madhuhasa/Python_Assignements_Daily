#first program
import re
print("Enter a paragraph(with at least 4 sentences)")
paragraph = str(input())

print("\nParagraph Entered :-")
print(paragraph)

paraList =[]
paraList = paragraph.split(".")

newPara=""
print("\nUpdating the middle sentence")
paraList[int(len(paraList)/2)] = "UST Global specializes in Healthcare, Retail & Consumer Goods, Banking & Financial Services, Telecom, Media & Technology, Insurance, Transportation & Logistics and Manufacturing & Utilities"
for i in range(len(paraList) -1):
    newPara +=paraList[i]
    newPara +="."
print(newPara)

countVowels = 0
countUpper = 0
countLower = 0
countSpecial = 0
countNum = 0

for ch in newPara:
    if ch.isalpha():
        if re.match("[AEIOUaeiou]",ch):
            countVowels += 1
        if ch.isupper():
            countUpper += 1
        elif ch.islower():
            countLower += 1
    elif ch.isnumeric():
        countNum += 1
    else:
        countSpecial+=1

wordDict = {}
wordList = []
wordList = newPara.split(" ")
for word in wordList:
    if wordDict.get(word):
        wordDict[word] += 1
    else:
        wordDict[word] = 1

print("\nNumber of Vowels: ",countVowels)
print("Number of Uppercases: ",countUpper)
print("Number of Lowercases: ",countLower)
print("Number of Special Characters: ",countSpecial)
print("\nRepeating Words and their frequency is as follows:-")
print("Word \t Frequency")
for key,value in wordDict.items():
    if(value > 1  and key!=" "):
        print("%s \t\t\t %d"%(key,value))

paraList = newPara.split(".")
tempPara = paraList[0]
paraList[0] = paraList[int(len(paraList))-2]
paraList[int(len(paraList))-2] = tempPara
newPara = ""
for i in range(int(len(paraList))-1):
    newPara += paraList[i]
    newPara +="."
print("\n New Paragraph after swapping first and last sentence")
print(newPara)


#second program

import statistics as stat
print("Enter student name and their corresponding marks in three subjects")
studentNameList = []
sub1List = []
sub2List = []
sub3List = []
for i in range(10):
    print("\nEnter Student %d Details"%(i+1))
    studentNameList.append(str(input("Enter student name: ")))
    sub1List.append(int(input("Enter subject 1 marks: ")))
    sub2List.append(int(input("Enter subject 2 marks: ")))
    sub3List.append(int(input("Enter subject 3 marks: ")))

print("\nStudent Details Registered as follows:-")
print("\nStudent Name \t Subject 1 \t Subject 2 \t Subject 3")
for i in range(10):
    print("%s \t\t\t %d \t\t\t %d \t\t\t %d"%(str(studentNameList[i]),int(sub1List[i]),int(sub2List[i]),int(sub3List[i])))

print("Median for Subject 1:",stat.median(sub1List))
print("Mean for Subject 1:",stat.mean(sub1List))

print("\nMedian for Subject 2:",stat.median(sub2List))
print("Mean for Subject 2:",stat.mean(sub2List))

print("\nMedian for Subject 3:",stat.median(sub3List))
print("Mean for Subject 3:",stat.mean(sub3List))

# Getting Grade Function
def getGrades(x):
    if(x>90):
        return "A+"
    elif(x>80):
        return "A"
    elif(x>70):
        return "B+"
    elif x>60:
        return "B"
    elif x>50:
        return "C"
    elif x<50:
        return "D"
    else:
        return "NotValid"

print("\nPrinting Student List along with their grades")
for i in range(10):
    print("\nStudent Name:",studentNameList[i])
    print("Subject 1:", getGrades(sub1List[i]))
    print("Subject 2:", getGrades(sub2List[i]))
    print("Subject 3:", getGrades(sub3List[i]))


#third program
    
def sortAndPrint(numList,x):
    numList.sort()
    flag = False
    for i in range(len(numList)):
        if (numList[i] == x):
            flag = True
            return ("Number found at position "+str(i + 1))
            break
    if flag == False:
        return ("Number not found")


x = [12,6,48,37,88,31,54,11,60,122,105,88,122,155,105]
print("Enter the number to search from the list ",x)

n = int(input())
x.sort()
flag=False
for i in range(len(x)):
    if(x[i]==n):
        flag=True
        print("Number found at position ",i+1)
        break
if flag == False:
    print("Element not found")

print("Try entering your own list")
print("How many numbers will you like to enter?")
numberList = []
n = int(input())
print("Please enter the numbers")
for i in range(n):
    numberList.append(int(input()))
print("Enter the number you will like to find")
print(sortAndPrint(numberList,int(input())))


#fourth program

print("Enter details of the family members")
memberName = []
memberAge = []
childrenGroup=[]
youthGroup = []
middleAge = []
seniorGroup = []
for i in range(20):
    print("Enter Name:")
    memberName.append(str(input()))
    print("Enter age:")
    memberAge.append(int(input()))
    print("\n")
    if(memberAge[i]>80):
        seniorGroup.append(str(memberName[i]))
    elif (memberAge[i]>45):
        middleAge.append(str(memberName[i]))
    elif (memberAge[i]>20):
        youthGroup.append(str(memberName[i]))
    else:
        childrenGroup.append(str(memberName[i]))
print("Family Members belonging to senior group")
for i in range(len(seniorGroup)):
    print(seniorGroup[i],end=", ")

print("\nFamily Members belonging to middle age group")
for i in range(len(middleAge)):
    print(middleAge[i],end=", ")

print("\nFamily Members who are still youth")
for i in range(len(youthGroup)):
    print(youthGroup[i],end=", ")
print("\nChildren in the family")
for i in range(len(childrenGroup)):
    print(childrenGroup[i],end=", ")


#fifth program
import statistics as stat
x=[11.95,11.91,11.86,11.94,12.00,11.93,12.00,11.94,12.10,11.95,11.99,11.94,11.89,12.01,11.99,11.94]
weightDict = {}
for i in x:
    if(weightDict.get(i)):
        weightDict[i] +=1
    else:
        weightDict[i]=1
print("Printing frequency distribution for the given data of actual liquid weight in 16 'twelve-ounces' cans")
print("Weight \t Frequency")
for key,value in weightDict.items():
    print("%f \t %d"%(key,value))

print ("Mean is :",stat.mean(x))
print("Median is:",stat.median(x))
print("Mode is:",stat.mode(x))

