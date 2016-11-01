"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array 
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
    	vis = {}
    	for i, num in enumerate(nums):#n would be the number, i would be the index
    		if num in vis and i-vis[num]<=k:
    			return True
    		vis[num] = i
    	return False
