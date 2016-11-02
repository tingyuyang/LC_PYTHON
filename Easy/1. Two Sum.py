"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
#Hash Table.Time: O(n), Space:O(n)
class Solution(object):
    def twoSum(self, nums, target):
        vis={}
    	for i, n in enumerate(nums):
    		rest =target-n
    		if rest in vis:
    			return vis[rest],i #因为题只要求2个数，所以简单很多！
    		vis[n]=i
