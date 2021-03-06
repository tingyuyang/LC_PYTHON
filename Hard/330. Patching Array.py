"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].
"""
#so basically, the individual element or the sum of those element should have result like->1,2,3,4,5,6,.....n.

#complexity: O(n)
def patching(nums,n):
	count=0
	i=0
	miss=1
	while miss<=n:
		if i<len(nums) and nums[i]<=miss: #*****remember i"<"len, instead of "<="
			miss+=nums[i]
			i=i+1
		else:
			print("the patch element should be:",miss)  #this line can help print out the which element will be added:)
			miss += miss
			count += 1
	return count
nums=[1,5,10]
n=20
print(patching(nums,n))
