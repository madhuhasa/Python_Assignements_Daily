# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:28:58 2018

@author: Madhuhasa
"""

#1. Python program to reverse a string using stack
 
# Function to create an empty stack. It initializes size of stack as 0
def createStack():
    stack=[]
    return stack
 
# Function to determine the size of the stack
def size(stack):
    return len(stack)
 
# Stack is empty if the size is 0
def isEmpty(stack):
    if size(stack) == 0:
        return True
 
# Function to add an item to stack . It increases size by 1    
def push(stack,item):
    stack.append(item)
 
#Function to remove an item from stack. It decreases size by 1
def pop(stack):
    if isEmpty(stack): return
    return stack.pop()
 
# A stack based function to reverse a string
def reverse(string):
    n = len(string)
     
    # Create a empty stack
    stack = createStack()
 
    # Push all characters of string to stack
    for i in range(0,n,1):
        push(stack,string[i])
 
    # Making the string empty since all characters are saved in stack    
    string=""
 
    # Pop all characters of string and put them back to string
    for i in range(0,n,1):
        string+=pop(stack)
         
    return string
     
# Driver program to test above functions
string="GeeksQuiz"
string = reverse(string)
print("Reversed string is " + string)
 

#2. Infix stack expressions
# Stack implementation
class Stack:
  
  # constructor for the Stack class
  def __init__(self):
    # initialise an empty list
    self.stack = []
    # self.stack = list() works the same way as above code
  
  # push the number into the stack
  def push(self, data):
    if data not in self.stack:
      self.stack.append(data)
      return True
    else:
      return False
    
  # remove the top element
  def pop(self):
    if len(self.stack) <= 0:
      return "Stack is empty!"
    else:
      return self.stack.pop()
    
  # returns the size of the element
  def size(self):
    return len(self.stack)
    
  # peek to see the top element
  def peek(self):
    return self.stack[-1]
    
  # to check if stck is empty
  def isEmpty(self):
    if len(self.stack) <= 0:
      return True
    else:
      return False
  
  # show the content of stack
  def show(self):
    return self.stack

# Simple method to apply operator to numbers
def applyOp(op, var2, var1):
  if op == '+':
    print ('Adding numbers...')
    return int(var1) + int(var2)
  elif op == '-':
    print ('Subtracting numbers...')
    return int(var1) - int(var2)
  elif op == '*':
    print ('Multiplying numbers...')
    return int(var1) * int(var2)
  elif op == '/':
    print ('Dividing numbers...')
    if var2 == 0:
      return "infinity"
    else:
      return int(var1) / int(var2)
  else:
    return 0

# check for precedence of operators
# returns True if op2 has higher precedence than op1
def hasPrecedence(op1, op2):
  if op2 == '(' or op2 == ')':
    return False
  elif (op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-'):
    return False
  else:
    return True

# Sample expression
expr = input("Enter the expression:")

# breaking down the expression into tokens
tokens = map(str, expr)
# removing the spaces from the list of tokens
tokens = ' '.join(tokens).split()

# stack to hold operands/numbers
var = Stack()
# stack to hold operators and parenthesis
ops = Stack()

# this is to inform the outer for loop
# to skip iteration for elements which together
# for a number, like 1,7 for 17
# we would not want 7 to be pushed again in our stack
skip = 0
for i in range(len(tokens)):
  # if skip is more than 0 skip the iteration
  if skip >= 1:
    # decrement skip flag
    skip -= 1
    continue
  # if we found a number
  if tokens[i] >= '0' and tokens[i] <= '9':
    num = tokens[i]
    # look for consecutive digits and append to num
    for j in range(i+1, len(tokens)):
      if tokens[j] >= '0' and tokens[j] <= '9':
        num = num + tokens[j]
        skip += 1
      else:
        break
    # push the number into var stack
    var.push(num)
    print (var.show())
  
  # if we find a opening parenthesis
  elif tokens[i] == '(':
    # add it to the ops stack
    ops.push(tokens[i])
  
  # if we find a closing parenthesis
  elif tokens[i] == ')':
    print ("Encountered closing parenthesis...")
    while ops.peek() != '(':
      # solve the expression uptil this point
      value = applyOp(ops.pop(), var.pop(), var.pop())
      if(value == "infinity"):
        print ("Invalid Expression")
        break
      else:
        print (value)
        var.push(value)
    ops.pop()
  
  # if we find any operator
  elif tokens[i] in ('+','-','*','/'):
    while ops.isEmpty() is False and hasPrecedence(tokens[i], ops.peek()):
      x = applyOp(ops.pop(), var.pop(), var.pop())
      print (x)
      var.push(x);
    # otherwise push the operator into ops stack
    ops.push(tokens[i]);
    print (ops.show())

# by this point entire expression has been parsed
# now apply operators to values stored in var stack
while(ops.isEmpty() is False):
  var.push(applyOp(ops.pop(), var.pop(), var.pop()));

# print the final result 
print ("Result of the expression is " + str(var.pop()))


#3.	Convert the following
#a.	a + b * (c ^ d - e) ^ ( f + g * h) -i    into postfix 

#from __future__ import division
#import random
OPERATORS = set(['+', '-', '^', '*', '/', '(', ')'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}
def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: output += stack.pop()
    print (output)
    return output
def evaluate_postfix(formula):
    stack = []
    for ch in formula:
        if ch not in OPERATORS:
            stack.append(float(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            c = {'+':a+b, '-':a-b, '*':a*b, '/':a/b}[ch]
            stack.append(c)
    print (stack[-1])
    return stack[-1]
if __name__ == '__main__':
    infix_to_postfix('a+b*(c^d-e)^(f+g*h)-i')
    
    
#Infix to Prefix
### INFIX ===> PREFIX ###
OPERATORS = set(['+', '-', '^', '*', '/', '(', ')'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}
def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.pop() # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.append(ch)
    
    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append( op+b+a )
    print (exp_stack[-1])
    return exp_stack[-1]
def evaluate_prefix(formula):
    exps = list(formula)
    while len(exps) > 1:
        for i in range(len(exps)-2):
            if exps[i] in OPERATORS:
                if not exps[i+1] in OPERATORS and not exps[i+2] in OPERATORS:
                    op, a, b = exps[i:i+3]
                    a,b = map(float, [a,b])
                    c = {'+':a+b, '-':a-b, '*':a*b, '/':a/b}[op]
                    exps = exps[:i] + [c] + exps[i+3:]
                    break
        print (exps)
    return exps[-1]
if __name__ == '__main__':
    infix_to_prefix('(a-b/c)*(a/k-l)')






#bt,wt,tat stands for burst time, waiting time, turn around time  respectively

print("Enter the number of processess: ")
n=int(input())
processes=[]
for i in range(0,n):
 processes.insert(i,i+1)

#Input Burst time of every process
print("\nEnter the burst time of the processes: \n")
bt=list(map(int, input().split()))

#Input Priority of every process
print("\nEnter the priority of the processes: \n")
priority=list(map(int, input().split()))
tat=[]
wt=[]

#Sorting processes burst time, on the basis of their priority
for i in range(0,len(priority)-1):
 for j in range(0,len(priority)-i-1):
  if(priority[j]>priority[j+1]):
   swap=priority[j]
   priority[j]=priority[j+1]
   priority[j+1]=swap

   swap=bt[j]
   bt[j]=bt[j+1]
   bt[j+1]=swap

   swap=processes[j]
   processes[j]=processes[j+1]
   processes[j+1]=swap

wt.insert(0,0)
tat.insert(0,bt[0])

#Calculating of waiting time and Turn Around Time of each process
for i in range(1,len(processes)):
 wt.insert(i,wt[i-1]+bt[i-1])
 tat.insert(i,wt[i]+bt[i])

#calculating average waiting time and average turn around time
avgtat=0
avgwt=0
for i in range(0,len(processes)):
 avgwt=avgwt+wt[i]
 avgtat=avgtat+tat[i]
avgwt=float(avgwt)/n
avgwt=float(avgtat)/n
print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,n):
 print(str(processes[i])+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
 print("\n")
print("Average Waiting time is: "+str(avgwt))
print("Average Turn Around Time is: "+str(avgtat))