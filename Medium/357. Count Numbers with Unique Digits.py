"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""

def count(n):
	list=[1,10,91]
	i=3
	result=list[i-1]
	plus=[0,9,81]
	while (i<=n):
		add=plus[i-1]*(9-i+2)
		plus.append(add)
		list.append(list[i-1]+plus[i])
		i=i+1
	return(list[n])
print(count(5))

#the list is: [1, 10, 91, 739, 5275, 32491...]
#The plus is: [0, 9, 81, 648, 4536, 27216...]----->[0, 9, 9*9, 9*9*8.....]       9*9*8=648
