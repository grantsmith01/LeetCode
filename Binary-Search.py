#Coded in AlgoMonster

'''
BINARY SEARCH GUIDE
1. Left flag is first index, right flag is last index. Mid is half of left + right, recalculate each loop
2. While left and right indices haven't passed each other, discard left half if arr[mid] is too low and right half if arr[mid] is too high
3. If arr[mid] = target, return mid.
4. Return -1 if target not found

NOTES
- O(log(N)) time complexity
- We discard half of the remaining array each iteration
'''

def binary_search(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
        
    return -1

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)
