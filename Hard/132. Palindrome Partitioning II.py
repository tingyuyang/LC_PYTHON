"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
#thoughts:http://blog.csdn.net/ljphhj/article/details/22573983
class Solution(object):
    def minCut(self, input):
        """
        :type s: str
        :rtype: int
        """
        l=len(input)
    	if(input==None or l==0):
    		return 0
    	cuts=[]
    	
    	#form a matrix with "l*l", set all value to FALSE
    	matrix=[[False for i in range(l)]for j in range(l)]
    	
    	#e.g l=5, l+1=6
    	#have cuts list:[6,5,4,...,0] <-with worst case
    	for i in range(0,l+1):
    		cuts.append(l-i)
    	
    	#matrix
    	for i in range(l-1,-1,-1):
    		for j in range(i,l):
    			if (input[i]==input[j] and (j-i)<2) or (input[i]==input[j] and matrix[i+1][j-1]==True):
    				matrix[i][j]=True
    				cuts[i]=min(1+cuts[j+1], cuts[i])
    	return cuts[0]-1
