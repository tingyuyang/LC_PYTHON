"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
def valid(s):
	stack=[]
	for ch in s:
		if ch =="(" or ch=="[" or ch=="{":
			stack.append(ch)
		else:
			if not stack:
				return False
			if ch==')' and stack[-1]!='(' or ch==']' and stack[-1]!='[' or ch=='}' and stack[-1]!='{':
				return False
			stack.pop()
	return not stack
s="()[]{}"
print(valid(s))  #True
s2="([)]"
print(valid(s2))   #False
