
'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
=====> You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

# this tricy mf
def longestConsecutive(nums):
    numSet = set(nums)
    res = 0
    for num in numSet:
        local_long = 0
        # checking if num is not a sequence starter
        if (num-1) not in numSet:
            local_long += 1
            # let's see how big sequence this num has
            while (num+1) in numSet:
                local_long += 1
                num += 1
        res = max(res, local_long)
    return res




######## good but does not work with negetive integers
# def longestConsecutive(nums):
#     space = [0 for _ in range(max(nums) + 1)]
#     res = 0
#     for num in nums:
#         space[num] = 1
#     count = 0
#     for occ in space:
#         if occ == 0:
#             res = max(count, res)
#             count = 0
#         else:
#             count += 1
#     res = max(count, res)
    
#     return res

# print(longestConsecutive([1,2,4,3,5]))