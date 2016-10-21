#http://bangbingsyb.blogspot.com/2014/11/leetcode-next-permutation.html
list=[7,2,5,2,3,1]
n=len(list)-1
for i in range(len(list)-1,-1,-1):
	if list[i]>list[i-1]: #NOTICE: list[i-1] is the item we want to swap!!!!
		for j in range(i,n):
			if list[j]>list[i-1] and list[i]>=list[j+1]:
				list[i-1],list[j]=list[j],list[i-1]
		break
print(list)
