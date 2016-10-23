"""
Given number of coins in an array , we need to arrange it on each stairs according to number of stairs and return the final stair which contains equal number of coins as of number of stair
Example - No of Coins : 4
Stair 1 - 1
Stair 2 - 2
Stair 3 - 1 

Returns = 2 , as stair 2 contain equal number of coins as of stair number.

sth like this

based on wiki:
https://en.wikipedia.org/wiki/Triangular_number
it gives u the function to judge if the input number is triangular number:
triNum=[math.sqrt(8*n+1)-1]//2

so if the triNum output is an int, it is an triangular number. 
based on the function we can easily come out the solution.
"""
import math
n=4 #n is the coin number
def arrangeCoins(n):
	y=math.sqrt(8*n+1)-1
	while y%2 !=0:
		n=n-1
		y=math.sqrt(8*n+1)-1
	return(y/2)
print(arrangeCoins(n))
