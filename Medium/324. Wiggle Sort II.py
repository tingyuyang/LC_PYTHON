"""

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
"""
       
#final solution
"""
after sort [1,2,3|4,5,6] <-slice into half, put into resultList from end for both half
after wiggle [3,6,2,5,1,4]

Also, need to consider the possiblity when --->len(result)=7,9,11(ODD number)
"""
class Solution(object):
    def wiggleSort(self, result):
        """
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        result.sort()
        sortList=result[:]
        i=0
        if len(result)%2==0:
        	j=len(result)//2-1
        else:
        	j=len(result)//2
        last=len(result)-1
        while (i<len(result)):
        	if i%2==1:
        		result[i]=sortList[last]
        		last-=1
        	else:
        		result[i]=sortList[j]
        		j-=1
        	i+=1
        print(result)

#-----------------------------------------------------------------------------------------------------------------------------
#first solution,kinda confused, coz they did not tell me whats the specific order they want?....
class Solution(object):
    def wiggleSort(self, result):
        """
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        result.sort()
        sortList=result[:]
        j=i=1 
        last=len(result)-1
        while (i<len(result)):
        	if i%2==1:
        		result[i]=sortList[last]
        		last-=1
        	else:
        		result[i]=sortList[j]
        		j+=1
        	i+=1
        print(result)
