"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

***so t is in another order of the letter in s, but same letter exactly
"""

#O(n log n) (:((()
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        a=sorted(s)
        b=sorted(t)
        for i in range(len(a)):
            if a[i]!=b[i]:
                return False
        return True
            
