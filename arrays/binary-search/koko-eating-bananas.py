'''
    what is the minimum number k "the banans per hour eating rate"
    
    so i want to create an algorithm which will return the minumum number k, which reduces k from every element in 'piles' until every element reaches zero that too one iteration at a time until h exhausts
    
    will be using binary search -- for this
    
    h decides the number of iterations (not really)
    
    Approach - 1:
    
    take h into frame and loop till it reaches 0.
    when h is zero that means we don't have any more time to eat bananas (to reduce an element by k)
    
    
    Example 1:

    Input: piles = [3,6,7,11], h = 8
    Output: 4
    
        why cannot k be the smallest possible number i.e. 1
        - because it will take 1*3 + 1*6 + 1*7 + 1*11 = 27 iterations or hours but h = 8
        
        what about k being 2:
        - then it will take for:
        - 3: ceil(3/2) -> 2 hours
        - 6: ceil(6/2) -> 3 hours
        - 7: ceil(7/2) -> 4 hours
        - 11: ceil(11/2) -> 6 hours
        which is 15 in total hours but our limit 'h' is 8 hours
        
        - too much time went, seeing the solution now
                - after seeing the NeetCode solution video i now understand that my intuition was right
    
    Final Approach:
    
    Intuition: The maximum value of k is the max(piles)
              - So we will apply binary search from 1 -> max(piles)
              
    - We will create a search space list from 1 to max(piles) and name it 'nums'
    
    - now we will apply binary search for this condition
        sum of ceil( element in piles / candidate from nums ) <= h
        
    '''


from math import ceil
import math

# first method
def min_eating_speed_v1(piles, h):
    
    # creating the searh space
    nums = [ele for ele in range(1, max(piles)+1)]
    
    # implementing binary-search on nums
    left, right = 0, len(nums)-1
    
    while left <= right:
        mid = (left + right) // 2
        candidate = nums[mid]
        
        # checking for every element in piles
        total_hrs = 0
        for pile in piles:
            total_hrs += ceil(pile / candidate)
            
        # now time for binary-search conditions
        '''
            it's important to understand the relation between the condition and eliminating search space
            - if total_hrs < h then that means the candidate is larger / ahead of k (the optimal candidate)
                - so we should ignore the right-subarray in nums -> right = mid - 1
            - in the other case where total_hrs > h we can ignore the left-subarray
                
        '''
        if total_hrs == h:
            return candidate
        elif total_hrs > h:
            left = mid + 1            
        else:
            right = mid - 1
                
# print(min_eating_speed([3,6,7,11], 8))


######################## the above method is not quite optimal some improvements are there
'''
    some improvements are there:
        - no need of creating search space
        - change in b-s condition
'''
# final method (optimal and correct)
def min_eating_speed_v2(piles, h):
    left, right = 1, max(piles)
    res = right # we know this is the worst case
    
    # the b-s algo
    while left <= right:
        candidate = (left + right) // 2
        total_hrs = 0
        
        # checking for every number in piles
        for pile in piles:
            total_hrs += math.ceil(pile / candidate)
        # now we have the total hours taken by our candidate 'rate' to finish all piles
        
        if total_hrs <= h:
            # if total_hrs is lesser than limit, that means our candidate rate was higher and we need to decrease it, so we will ignore the right-subarray and search for candidate in the left-subarray
            # result has to be minimum 
            res = candidate
            right = candidate - 1
        else:
            left = candidate + 1
    
    return res
    

print(min_eating_speed_v2([3,6,7,11], 8))

