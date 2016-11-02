# Set
```python
a = set('abracadabra')
>>> a                                  # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
```
## Example 1
```python 
s= "anagram"
a=set(s)
print(a) #{'r', 'g', 'm', 'n', 'a'} ****the order of the print out will be different each time!!
```
## Example 2
```python
s= "anagram"
vis= {}
for i, l in enumerate(s):
	vis[l]=i 
print(vis) #{'n': 1, 'g': 3, 'r': 4, 'm': 6, 'a': 5}
