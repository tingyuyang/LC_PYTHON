def missingNumber(self, nums):
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)-1):
            if nums[i] != (nums[i-1]+1):
                return nums[i]
