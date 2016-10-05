"""
Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Return the array [2, 1, 1, 0].
"""
#simple solution with O(N^2) complexity

class Solution(object):
    def countSmaller(self, nums):
        countList =[]
        for i in range(len(nums)):
        	count = 0
        	for j in range (i+1,len(nums)):
        		if nums[i]>nums[j]:
        			count+=1
        	countList.append(count)
        return(countList)
    
#Merge sort
def countSmaller(nums):
    def merge_sort(enums):
        mid = int(len(enums)/2)
        if mid>=1:
            nums1, nums2 = merge_sort(enums[:mid]), merge_sort(enums[mid:])
            i, j = 0, 0

            while i < len(nums1) or j < len(nums2):
                if j == len(nums2) or i < len(nums1) and nums1[i][1] <= nums2[j][1]:
                    res[nums1[i][0]] += j
                    enums[i + j] = nums1[i]
                    i += 1
                else:
                    enums[i + j] = nums2[j]
                    j += 1
        return enums
    res = [0]*len(nums)
    a = merge_sort(list(enumerate(nums)))
    return res
a=[5,2,6,1]
print(countSmaller(a))
