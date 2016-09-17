"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question

my analysis:
do not need to remove the duplicated item, can just exchange the next non repeated item:
[1,1,2] ->>>> [1,2,1]
最后还是用了网上的方法，本来自己想从最后往前算，但是[1,1,1,2],这样就不行
网上方法死也看不懂，最终还是自己在纸上实践才真正懂了。
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
