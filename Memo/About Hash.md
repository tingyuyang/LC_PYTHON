# Hash

* Differentiate b/w hash table and hash set.
* My practice w/ Hash:
  * [Contains Duplicate( HashSet )](https://github.com/tingyuyang/python_lc/blob/master/Easy/217.%20Contains%20Duplicate.py)
  * [Two Sum](https://github.com/tingyuyang/python_lc/blob/master/Easy/1.%20Two%20Sum.py)
* [About Set](https://github.com/tingyuyang/python_lc/blob/master/Memo/About%20Set.md)
	* [Information about "Set()" in Python](http://www.learnpython.org/en/Sets)
## E.g.(Hash will put NUMBER in order, but not LETTERS)(<-还需要研究下。。。)
```python
nums=[11,15,2,100]
vis = {}
for i, num in enumerate(nums):
    vis[num] = i
print(vis) #{2: 2, 11: 0, 100: 3, 15: 1}
```
