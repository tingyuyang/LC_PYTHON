"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
#My analysis:
"""
This is such a weird question.....
if input is[0,1], you need to return 2.....like WHY?
the question did not ask on POINT...****like WHAT EXACTLY ARE U ASKING HERE?!****   

so simple math used here (首项 + 末项) * 项数 / 2
NOTICE:the input might not be in order
"""
#final solution:
class Solution(object):
    def missingNumber(self, nums):
        sum=0
        for n in nums:
            sum+=n
        expect=(1+len(nums))*len(nums)/2
        return (expect-sum)



#my first wrong attempt, thought the list is in order
"""
def missingNumber(self, nums):
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)-1):
            if nums[i] != (nums[i-1]+1):
                return nums[i]
"""
