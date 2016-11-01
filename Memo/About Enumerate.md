# Enumerate

### Example 1:
```
nums=[1,2,1,4,5]
for i,nums[i] in enumerate(nums): 
   print (i ,nums[i])
```
* print out:
```
0 1
1 2
2 1
3 4
4 5
```
### Example 2
```
nums=[1,2,3,4,5]
vis = {}
for i, num in enumerate(nums):
	vis[num] = i
	print(num,i)
print(vis)
```
Print Out:
```
1 0
2 1
3 2
4 3
5 4
{1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
```
