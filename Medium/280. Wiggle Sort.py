"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]….

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
"""
list=[3, 5, 2, 1, 6, 4]
def wiggle(list):
	list.sort()
	i=0
	k=0
	j=len(list)-1
	result=[]
	while len(result) < len(list):
		if i %2 ==0:
			result.append(list[k])
			k+=1
		else:
			result.append(list[j])
			j-=1
		i+=1
	return(result)
print(wiggle(list))
