

class Solution:
    def trap(self, height) -> int:
        lm, rm = 0, 0
        l, r = 0, len(height)-1
        water = 0
        while l <= r:
            if height[l] <= height[r]:
                comp = lm - height[l]
                water += comp if comp > 0 else 0
                lm = max(height[l], lm)
                l += 1
            else:
                comp = rm - height[r]
                water += comp if comp > 0 else 0
                rm = max(height[r], rm)
                r -= 1

        return water



print(
    Solution().trap(
        [0,1,0,2,1,0,1,3,2,1,2,1]
    )
)




'''

class Solution:
    def trap(self, height) -> int:
        # using a O(N) space complexity
        LeftMax = []
        RightMax = [0 for _ in range(len(height))]
        lm, rm = 0, 0
        water = []

        for num in height:
            LeftMax.append(lm)
            lm = max(lm, num)
        
        for i in range(len(height)-1, -1, -1):
            num = height[i]
            RightMax[i] = rm
            rm = max(rm, num)
            
        for i in range(len(height)):
            water.append(min(LeftMax[i], RightMax[i]) - height[i])
        
        res = sum([amt if amt > 0 else 0 for amt in water])
        # above line is equivalent to 
        # newArr = []
        # for amt in water:
        #   if amt > 0:
        #       newArr.append(amt)
        #   else:
        #       newArr.append(0)
        # res = sum(newArr)
        
        return res
        
        
# print(
#     Solution().trap(
#         [0,1,0,2,1,0,1,3,2,1,2,1]
#     )
# )

'''