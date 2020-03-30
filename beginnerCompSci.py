#prefix sum base
original = list(map(int, input().split()))#takes a list of integers 
prefixsumarray = []#creates an array for the prefix sum
prefixsumarray[0] = original[0]#start off the array before the loop
for i in range(len(original)):#every time
  prefixsumarray[i] = prefixsumarray[i-1] + original[i]#int is the previous int plus the num from original
def getSum(a, b):#sum equals
  prefixsumarray[a] - prefixsumarray[b] + original[b]

#power recursion example
def power(base, exponent):
	#BASE CASE: x^0 = 1
	if exponent == 0:
		return 1
	#BODY: manipulate variable from base by calling self
	else:
		return base * power(base, exponent - 1)


