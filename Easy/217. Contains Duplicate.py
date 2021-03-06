"""
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False

# Use Hash:
# Hash set more specifically
class Solution(object):
    def containsDuplicate(self, nums):
        vis =set()
    	for n in nums:
    		if n in vis:
    			return True
    		vis.add(n)
    	return False
