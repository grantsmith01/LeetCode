#Coded on AlgoMonster

'''
- The minimum amount of time it would take would be max(arr) in the case of len(arr) coworkers.
- The maximum amount of time it would take would be sum(arr) in the case of 1 coworker.
- The optimal amount of time would be between these two values, so make a binary search between these, 
  setting minimum as left flag and maximum as right flag.
- We want to test mid values, checking if they're even enough time for the designated number of coworkers
  to get through the newspapers. This is the condition that sets array to left side false, right side true.
- 
'''

def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = max(newspapers_read_times)    #minimum possible amount of time, given len(arr) coworkers
    right = sum(newspapers_read_times)   #maximum possible amount of time, given 1 coworker
    min_time = right  #tracker for current lowest possible time for coworkers to read
    while left <= right:
        mid = (left + right) // 2
        if enoughTime(newspapers_read_times, num_coworkers, mid):  #if there's enough time per coworker, shift left to find a possible new minimum time
            min_time = mid
            right = mid - 1
        else:  #if there is not enough time for coworkers to read all newspapers, shift right to give them more time
            left = mid + 1
    return min_time  #upon finding boundary of condition, left will become > right and loop will time out

def enoughTime(newspapers_read_times: List[int], num_coworkers: int, given_time: int) -> bool:
    #HELPER FUNCTION TO CHECK CONDITION
    time_left = given_time
    current_coworker = 1  #flag to track how many coworkers we've gone thru. first coworker is coworker 1
    for i in range(len(newspapers_read_times)):
        if time_left - newspapers_read_times[i] >= 0:  #if there's enough time left, read it and decrement time left by time to read current newspaper
            time_left -= newspapers_read_times[i]
        else:  #not enough time left for current coworker to read through current newspaper at index i
            current_coworker += 1
            time_left = given_time - newspapers_read_times[i]
    return current_coworker <= num_coworkers  #return condition stated above
