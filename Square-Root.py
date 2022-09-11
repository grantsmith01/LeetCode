#Coded on AlgoMonster

'''
Given an integer, find its square root without using the built-in square root function. Only return the integer part (truncate the decimals).

EXAMPLES
Input: 16

Output: 4

Input: 8

Output: 2

Explanation: square root of 8 is 2.83..., return integer part 2

NOTES
- This is another example of finding the boundary of a certain condition. Here, the condition is mid^2 <= n. We want to find the last value of mid that
  satisfies this condition, since anything over wouldn't qualify. Find boundary, erorr on left side since we're truncating decimals of real square root
'''

def square_root(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    right = n
    sqrt = 0
    while left <= right:
        mid = (left + right) // 2
        if mid**2 <= n:
            sqrt = mid
            left = mid + 1
        else:
            right = mid - 1
    return sqrt

if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)
