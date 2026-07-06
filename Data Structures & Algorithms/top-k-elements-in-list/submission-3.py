class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 0
            hashmap[n] += 1

        # create a min-heap and pop the k frequent elements
        heap = []
        for key in hashmap.keys():
            heapq.heappush(heap, (hashmap[key], key))
            # place the sorting key as the first element of the tuple

            if len(heap) > k:
                heapq.heappop(heap)
                # in a min-heap, heappop removes the SMALLEST element
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
            
        return ans
    
    # time complexity: O(nlogn)
    # space complexity:

    def topKFrequentWithBucketSort(self, nums: List[int], k: int) -> List[int]:
        # make a frequency map
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 0
            hashmap[n] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)] 
        # [[]]*(len(nums) + 1) is WRONG: this creates multiple references to the same list object
        # since frequency can range from 0 to n, the bucket array needs a size of n + 1

        for num, count in hashmap.items():
            bucket[count].append(num) # do not overwrite since numbers can appear the same frequency
        
        # when choosing the top k elements, use bucket sort to keep the time complexity O(n)
        ans = []
        for i in range(len(bucket)-1, 0, -1):
            if bucket[i] != []:
                for val in bucket[i]:
                    ans.append(val)
                # ans.append(bucket[i]) is WRONG

            if len(ans) == k:
                break

        return ans


    # time complexity: O(n) since this solution uses O(n) sorting algorithm(bucket sort)
    # space complexity: O(n) because of the frequency map that has the same length as nums

    # when asked to find the kth smallest or largest elements, the first method that comes to mind is to use a min/max heap or sorting