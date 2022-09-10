#Coded in AlgoMonster

'''
BUBBLE SORT GUIDE
1. Loop through all elements except for last, since we'll be comparing current with current+1
2. Set a "swapped" variable to indicate whether or not we've swapped in the coming loop
3. Loop through all elements except for last few that have already been sorted
4. Compare current element to next. If it's greater, swap and set swapped variable to true
5. !!!If the current element is NOT greater, it won't swap and next element will become current and have the chance to bubble up.
6. After the entire inner loop, break and return if nothing was swapped, indicating that the list is already sorted

NOTES
- O(n^2) time complexity
- Fast for nearly sorted lists since it has the swapped flag, near O(1)

'''

def bubble_sort(unsorted_list: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    for i in range(len(unsorted_list)-1):
        swapped = False
        for j in range(len(unsorted_list)-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
                swapped = True
        if swapped == False:
            break
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = bubble_sort(unsorted_list)
    print(' '.join(map(str, res)))
