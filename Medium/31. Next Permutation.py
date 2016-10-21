#http://bangbingsyb.blogspot.com/2014/11/leetcode-next-permutation.html
#kinda right thought, but not correct exactly!!!
"""
1. find from the list[end-1] to list[0] order 
	i. find if any list[i]<list[i+1]    (e.g. 523,2>3)
	   break the for loop
	ii. if not, it means the list already dictionary end.
	    reverse the list
2. find j between in list[i:end]
	- which list[j]>list[i]          	     (e.g. 5231), list[i] =2, list[j] =3
	- switch list[j] and list[i]		=>[5,3,2,1]
3. sort the item in order after list[i] (5321, list[i]=3, sort(21))
	list[i+1:]=sorted(list[i+1:])
"""
#---------------------------------------------SOLUTION 1
list=[5,2,3,1] #->[5,3,1,2] is correct
def nextPermutation(list):
	checkBreak= False
	for i in range(len(list)-2,-1,-1):
		if list[i]<list[i+1]: 
			checkBreak=True
			break
	if not checkBreak:
		list.reverse()
		return list
	for j in range(len(list)-1,i,-1):
		if list[j]>list[i]:
			list[i],list[j]=list[j],list[i]
			break
	#=>[5,3,2,1]
	list[i+1:]=sorted(list[i+1:])
	return list
print(nextPermutation(list))

#---------------------------------------------SOLUTION 2, ONLY DIFFERENCE: last for loop
list=[5,2,3,1] #->[5,3,1,2] is correct
def nextPermutation(list):
	n=len(list)-1
	checkBreak= False
	for i in range(len(list)-2,-1,-1):
		if list[i]<list[i+1]: 
			checkBreak=True
			break
	if not checkBreak:
		list.reverse()
		return list
	for j in range(len(list)-1,i,-1):
		if list[j]>list[i]:
			list[i],list[j]=list[j],list[i]
			break
	#=>[5,3,2,1]
	for j in range(0, (len(list) - i)//2):
	    list[i+j+1], list[len(list)-j-1] = list[len(list)-j-1], list[i+j+1]
	print (list)
print(nextPermutation(list))
