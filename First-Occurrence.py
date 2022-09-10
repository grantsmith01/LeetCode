#Coded on AlgoMonster

'''
Find Element in Sorted Array with Duplicates
Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. 
Return -1 if the target is not in the array.

EXAMPLES
Input:

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3
Output: 1

Explanation: First occurrence of 3 is at index 1.

Input:

arr = [2, 3, 5, 7, 11, 13, 17, 19]
target = 6
Output: -1

Explanation: 6 does not exists in the array.
'''

def find_first_occurrence(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    right = len(arr)-1
    firstOcc = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            firstOcc = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return firstOcc

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)
