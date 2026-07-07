import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a min heap of size k
        # keep adding elements, and the min element left in the heap after iterating through all elements is the kth largest

        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n) # O(log(k+1))
            if len(min_heap) > k:
                heapq.heappop(min_heap) # O(logk)

        return min_heap[0]

        # time: O(nlogk) n * tree of size k 
        # space: O(k)