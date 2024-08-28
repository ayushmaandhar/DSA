class Solution:
    def max_points(self, points) -> int:
        return 1
    
    def brute_force(self, points) -> int:
        prev = points[0]
        score = 0
        
        # choose maximum from prev 
        for m in range(1,len(points)):
            curr = points[1]
            for n in range(len(points[m])):
                
        