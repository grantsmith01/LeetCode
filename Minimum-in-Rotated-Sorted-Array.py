#Coded on AlgoMonster

'''
EXPLANATION
You need a point of reference to be able to tell where you should be going. Since we can't use the elements around us, as that would not be linear,
we will use one fixed point in the array: the last element. If the last element is bigger than us (the current value), then the valley should be to our left as it slopes down
to the left. Move right pointer to current - 1. If the last point is smaller than us, the valley must be to our right. Move left pointer up + 1.

'''

def find_min_rotated(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid-1] and arr[mid] < arr[mid+1]:
            break
        elif arr[mid] > arr[len(arr)-1]:
            left = mid + 1
        else:
            right = mid - 1
    return mid


#1 2 3 4 5
#2 3 4 5 1
#3 4 5 1 2
#4 5 1 2 3
#5 1 2 3 4

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)
