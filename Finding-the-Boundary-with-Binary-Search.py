#Coded in AlgoMonster

def find_boundary(arr: List[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    right = len(arr)-1
    boundary = -1                   #set a boundary to keep track of leftmost True value. set to -1 in case no True val is ever found
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:                
            boundary = mid          #set boundary to each True value as you continue left towards the final boundary
            right = mid - 1
        else:
            left = mid + 1 
    return boundary                 #once left and right pass each other, loop will terminate and last found True value index will be returned, which is leftmost boundary!

if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)
