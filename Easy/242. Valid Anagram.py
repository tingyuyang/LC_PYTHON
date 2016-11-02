"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

***so t is in another order of the letter in s, but same letter exactly
"""
#本以为自己给的最差解，没想到网上都这么写的
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
#Shorter Version(真是有够短的，哈哈哈)
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s)==sorted(t)

    
# Still O(n log n)
def isAnagram(self, s, t):
        from collections import Counter
        return Counter(s) == Counter(t)
