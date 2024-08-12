import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # declaring member variables
        self.minHeap, self.k = nums, k
        # converting array into minHeap
        heapq.heapify(self.minHeap)
        # only keeping (k or less) elements in the heap
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)