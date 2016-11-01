"""
use dp(dynamic programming) here!
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
