#Coded in AlgoMonster

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
