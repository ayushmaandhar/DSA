
def algo(nums, target) -> int:
    # so the basic idea is to divide and conquer, but the array needs to be SORTED!!!!!!
    # intuition is: if target is smaller than the middle element that means the right subarray can be removed from searching space
    # and if target is larger than the middle element then left subarray can be removed from searching sample space
    # now the new smaller array is left to again implement the same logic. 
    
    # we will have three pointers: left, right, mid
    
    left = 0
    right = len(nums)-1

    # the loop will run until left and right pointer meet
    while left <= right:
        mid = (left + right) // 2 # integer division
        print("l->",nums[left]," m->",nums[mid]," r->",nums[right])
        
        if nums[mid] == target:
            return mid 
        elif target < nums[mid]: # this means the target is in left sub-array
            right = mid - 1
        else: # target > nums[mid] (target is in right sub-array)
            left = mid + 1
    # if array traversed but target not found then return -1
    return -1


# let's check this
arr = [1,2,3,4,5,6,7]
print(algo(arr,7.1))
    