#Coded on AlgoMonster

'''
Condition here is to find the lowest maxWeight while days == d.
To divide the array into a condition of half false and half true, left side being false and right being true,
the condition must be that days to ship <= designated days. Find leftmost day that qualifies, leftmost being
the day with the minimum weight that achieves shipping in the designated amount of days.
If days to ship > designated days, that means the weight limit is too low, so shift right

- Condition to half the array into trues and falses: days to ship <= designated days.
- If it takes too few days to ship, then minWeight is too high, and we need to lower it by shifting right 
  indicator to the left. Trues half of the array
- If it takes just the right amount of days to ship, then we're nearing our true minWeight by shifting left.
- If it takes too many days to ship, our minWeight is too low, and we need to up it by shifting left indicator
  to the right. Falses half of array
'''

def min_max_weight(weights: List[int], d: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = max(weights) #minimum weight capacity of truck
    right = sum(weights) #maximum weight capacity of truck
    minWeight = 0
    while left <= right:
        mid = (left + right) // 2
        if feasible(weights, d, mid):  #if days less than or equal to d, shift left to find minimum qualifying weight
            minWeight = mid  #even if days > d, we'll be shifting ever-left to find condition where ultimately days = d
            right = mid - 1
        else:  #otherwise, days is less than d, so shift right to find correct range of days
            left = mid + 1
    return minWeight

def feasible(weights: List[int], d: int, maxWeight: int) -> bool:
    days = 1                         #set to 1 initially because first day is unaccounted for in loop
    capacity = maxWeight
    for i in range(len(weights)):
        if weights[i] <= capacity:  #enough capacity
            capacity -= weights[i]
        else:                       #not enough capacity, increase day and reset capacity
            days += 1
            capacity = maxWeight - weights[i]
    return days <= d

if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    d = int(input())
    res = min_max_weight(weights, d)
    print(res)
