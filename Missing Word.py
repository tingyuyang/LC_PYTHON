"""
#GoDaddy
s="i am using books"
t="am books"

print out what is missing b/w s and t:
i using 
"""
s="i am using books"
t="am books"
def missingWord(s,t):
	i=0
	j=0
	result=""
	while i <len(s):
		if s[i]!=t[j]:
			result+=s[i]
		else:
			j=j+1
		i+=1
	return result
print(missingWord(s,t))
#i using 
