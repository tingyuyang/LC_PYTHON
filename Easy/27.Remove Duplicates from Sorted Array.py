"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question
"""
class Solution:
    def removeDuplicates(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(n)==0:
            return 0
        j=0
        for i in range(0,len(n)):
        	if n[i]!=n[j]:
        		n[j+1],n[i]=n[i],n[j+1]
        		j=j+1
        return j+1
