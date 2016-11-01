"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array 
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
    	vis = {}
    	for i, num in enumerate(nums):#num would be the number, i would be the index
    		if num in vis and i-vis[num]<=k:
    			return True
    		vis[num] = i
    	return False
"""
e.g. 
nums=[1,2,1,4,5]
1 0
2 1
1 2
4 3
5 4
{1: 2, 2: 1, 4: 3, 5: 4}

so "num would be the number, i would be the index"
but in hash table is totally opposite
"""
