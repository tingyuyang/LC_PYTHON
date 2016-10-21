#http://bangbingsyb.blogspot.com/2014/11/leetcode-next-permutation.html
def nextPermutation(list):
	n=len(list)-1
	for i in range(len(list)-1,-1,-1):
		if list[i]>list[i-1]: #NOTICE: list[i-1] is the item we want to swap!!!!
			break
	else:
		list.reverse()
		return list
	for j in range(i,n):
		if list[j]>list[i-1]:
			list[i-1],list[j]=list[j],list[i-1]
	#list will be [5,3,2,1] here
	
	i=i-1
	#print(list[i+0+1])
	#print(list[len(list)-0-1])
	for j in range(0, (len(list) - i)//2):
	    list[i+j+1], list[len(list)-j-1] = list[len(list)-j-1], list[i+j+1]
	print(list)
	return (list)
nextPermutation(list)
