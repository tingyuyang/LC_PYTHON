#http://bangbingsyb.blogspot.com/2014/11/leetcode-next-permutation.html
#kinda right thought, but not correct exactly!!!
"""
1. find from the list[end] to list[0] order 
	i. find if any list[i]>list[i-1]    (e.g. 523,2>3)
	   break the for loop
	ii. if not, it means the list already dictionary end.
	    reverse the list
2. 
"""
list=[5,2,3,1] #->[5,3,1,2] is correct
def nextPermutation(list):
	n=len(list)-1
	for i in range(len(list)-1,-1,-1):
		if list[i]>list[i-1]: 
			break
	else:
		list.reverse()
		return list
	for j in range(n,i-1,-1):
		if list[j]>list[i-1]:
			list[i-1],list[j]=list[j],list[i-1]
			break
	i=i-1
	for j in range(0, (len(list) - i)//2):
	    list[i+j+1], list[len(list)-j-1] = list[len(list)-j-1], list[i+j+1]
	print(list)
	return (list)
nextPermutation(list)
