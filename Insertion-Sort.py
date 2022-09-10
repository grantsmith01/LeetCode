#Coded in AlgoMonster

'''
INSERTION SORT GUIDE
1. Left side of list is sorted, right side is unsorted
2. Loop through array starting from index 1. 
3. Each iteration, make a while loop that checks if current index is greater than 0; if it is, check if current element is LESS than previous element
4. Swap current element with previous if current element is LESS than previous element.
5. Decrement current variable. Once "current" variable, which is initially set to i, reaches 0 then while loop terminates

NOTES
- Insertion sort sweeps left to right but current element will shift right to left as it is sorted
- Fast for lists that are already almost sorted, close to O(1)
- It is a stable algorithm because later elements will not swap with earlier elements unless the later element is smaller
- It is an in-place algorithm because no additional data structure is used to store intermediate values.
- O(n^2) time complexity
'''

def sort_list(unsorted_list: List[int]) -> List[int]:
    for i in range(1, len(unsorted_list)):
        curr = i
        while curr > 0 and unsorted_list[curr] < unsorted_list[curr-1]:
            temp = unsorted_list[curr]
            unsorted_list[curr] = unsorted_list[curr-1]
            unsorted_list[curr-1] = temp
            curr -= 1
                
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
