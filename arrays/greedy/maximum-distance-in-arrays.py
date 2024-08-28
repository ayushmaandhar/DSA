class Solution:
    def maxDistance(self, arrays):
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            max_distance = max(max_distance, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0]))
            if arrays[i][0] < min_val:
                min_val = arrays[i][0]
            if arrays[i][-1] > max_val:
                max_val = arrays[i][-1]
                
        return max_distance
