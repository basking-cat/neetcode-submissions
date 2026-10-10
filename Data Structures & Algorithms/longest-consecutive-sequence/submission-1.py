class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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

        # t: O(n)
        # s: O(n)