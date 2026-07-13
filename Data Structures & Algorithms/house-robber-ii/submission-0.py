class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_sub(houses: List[int]) -> int:
            prev2, prev1 = 0, 0
            for h in houses:
                prev2, prev1 = prev1, max(prev2 + h, prev1)
            return prev1

        if len(nums) == 1:
            return nums[0]

        return max(rob_sub(nums[:-1]), rob_sub(nums[1:]))

        # time: O(n)
        # space: O(1) - slice operation is 'view'