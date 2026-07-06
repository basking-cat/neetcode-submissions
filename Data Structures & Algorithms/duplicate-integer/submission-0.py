from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for n in c.values():
            if n > 1:
                return True
        return False