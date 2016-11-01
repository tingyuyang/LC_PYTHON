"""
use DP(dynamic programming) here!

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

reference w/ good explanation:
http://www.qiujiawei.com/leetcode-problem-198/
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
    	dp=[0]*(size+1) #view dp as f(x) list, dp(0)=a*0+b, dp(1)=a*1+b.....
    	if size>0:
    		dp[0]=0
    		dp[1]=nums[0] 
    		#dp(0)=0,we can steal nothing before house0, 
    		#dp(1)=house0,we can only steal most from house0
    	for i in range(2,size+1):
    		dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])
    		#f(3) = max(nums[1], nums[0] + nums[2])
    	return dp[size]

#because we're not required to print out the whole dp list, we can have another solution w/ LESS SPACE complexity
class Solution(object):
    def rob(self, nums):
        size = len(nums)
    	if size==0:
    		return 0 
    	elif size==1:
    		return nums[0]
    	pre=0 
    	cur=0 
    	temp=-1 
    	for i in range(0,size):
    		temp=cur
    		cur=max(nums[i]+pre,cur)
    		pre=temp
    	return cur
