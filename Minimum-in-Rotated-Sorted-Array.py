#Coded on AlgoMonster

'''
A sorted array of unique integers was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. 
Find the index of the minimum element in this array. All the numbers are unique.

Input: [30, 40, 50, 10, 20]

Output: 3

Explanation: the smallest element is 10 and its index is 3.

Input: [3, 5, 7, 11, 13, 17, 19, 2]

Output: 7

Explanation: the smallest element is 2 and its index is 7.

NOTES
You need a point of reference to be able to tell where you should be going. Since we can't use the elements around us, as that would not be linear,
we will use one fixed point in the array: the last element. If the last element is bigger than us (the current value), then the valley should be to our left as it slopes down
to the left. Move right pointer to current - 1. If the last point is smaller than us, the valley must be to our right. Move left pointer up + 1.
- The condition here is if the element is less than the last element. Must find the first time this is true
'''

def find_min_rotated(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    right = len(arr) - 1
    boundary_index = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[len(arr)-1]:     #THIS CONDITION MUST BE LESS THAN OR EQUAL! If not, once it reaches the smallest element it won't set index
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_tracker


#1 2 3 4 5
#2 3 4 5 1
#3 4 5 1 2
#4 5 1 2 3
#5 1 2 3 4

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)
