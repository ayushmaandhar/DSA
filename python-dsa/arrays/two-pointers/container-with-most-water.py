class Solution:
    
    def maxArea(self, height) -> int:
        # let's create a method to calculate water
        def water_in_container(r, l):
            return (r-l) * min(height[r], height[l])
        
        # let's be greedy with two pointers
        max_water = 0
        l, r = 0, len(height)-1
        while l <= r:
            max_water = max(max_water, water_in_container(r, l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water
    
print(
    Solution().maxArea([2,3,4,5,18,17,6])
)