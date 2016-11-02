# Hash

* Differentiate b/w hash table and hash set.
* My practice w/ Hash:
  * [Contains Duplicate( HashSet )](https://github.com/tingyuyang/python_lc/blob/master/Easy/217.%20Contains%20Duplicate.py)
* [Information about "Set()" in Python](http://www.learnpython.org/en/Sets)

## Example 1
```python
s= "anagram"
vis= {}
for i, l in enumerate(s):
	vis[l]=i 
print(vis)
```
```
{'n': 1, 'g': 3, 'r': 4, 'm': 6, 'a': 5}
```
