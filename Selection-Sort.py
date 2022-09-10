#Coded in AlgoMonster

'''
SELECTION SORT GUIDE
1. Loop through entire list. Each iteration set the minimum's index to current element
2. Each iteration of outer loop, loop through all the remaining elements after current element
3. Upon each iteration of inner loop, check if current inner loop element is LESS than minimum element. If it is, set new minimum index
4. After exiting inner loop, swap the new minimum element with the current outer loop element

NOTES
- NOT fast when list is already almost sorted. Time complexity will always be O(n^2)
- This algorithm is not stable because an earlier element can jump after an element of the the same value during a swap
- The algorithm is in place as it only needs additional memory to store the index to the minimum element.
'''

def selection_sort(unsorted_list: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    for i in range(len(unsorted_list)):
        minimum = i
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[minimum]:
                minimum = j
        temp = unsorted_list[i]
        unsorted_list[i] = unsorted_list[minimum]
        unsorted_list[minimum] = temp
                
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    #res = insertion_sort(unsorted_list)
    res = selection_sort(unsorted_list)
    print(' '.join(map(str, res)))
