"""
Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Return the array [2, 1, 1, 0].
"""
#simple solution with O(N^2) complexity

class Solution(object):
    def countSmaller(self, nums):
        countList =[]
        for i in range(len(nums)):
        	count = 0
        	for j in range (i+1,len(nums)):
        		if nums[i]>nums[j]:
        			count+=1
        	countList.append(count)
        return(countList)
