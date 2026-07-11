class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        two_houses_before = nums[0]
        one_house_before = max(two_houses_before, nums[1])

        current = 0
        for i in range(2, n):
            current = max(two_houses_before + nums[i], one_house_before)
            two_houses_before = one_house_before
            one_house_before = current

        return current

        # time: O(n)
        # space: O(1)