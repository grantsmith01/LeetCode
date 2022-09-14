#Coded on AlgoMonster

'''
NOTES
- The essence of binary search problems is boiling the array down to booleans - true and falses - and finding the boundary where the first true occurs
- Here, the condition for before boundary (falses) and after boundary (trues) is whether or not the current element is greater than the next
- On the first time this condition is true, that's the peak. Because to the left of the peak, current element is always less than the next
- While loop condition will fail once peak is found and boundary index will be returned

'''

def peak_of_mountain_array(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    right = len(arr) - 1
    boundary_index = 0;
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid+1]: #I am greater than the next element, sloping down
            boundary_index = mid
            right = mid - 1
        else:  #arr[mid] < arr[mid+1] I am lesser than the next element, sloping up
            left = mid + 1
    return boundary_index #while loop will fail conditions once peak was reached and return true boundary index

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)
