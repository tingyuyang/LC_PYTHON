#http://bangbingsyb.blogspot.com/2014/11/leetcode-next-permutation.html
#kinda right thought, but not correct exactly!!!
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
