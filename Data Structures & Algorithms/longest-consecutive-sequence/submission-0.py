class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store every element in a set
        # for each element, look up "current - 1" in the set
        # if found in the set, subtract 1 and repeat until the last consecutive element

        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            cur = n
            max_len = 1
            if cur - 1 in nums_set:
                continue
            
            while cur + 1 in nums_set:
                cur += 1
                max_len += 1
            longest = max(longest, max_len)

        return longest