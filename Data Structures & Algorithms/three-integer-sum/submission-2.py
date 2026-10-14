class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        ret = []
        nums_sorted = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
                
            l, r = i+1, len(nums) - 1
            mini_target = target - nums_sorted[i]

            while l < r:
                cur_sum = nums_sorted[l] + nums_sorted[r]
                if cur_sum < mini_target:
                    l += 1
                elif cur_sum == mini_target:
                    ret.append([nums_sorted[i], nums_sorted[l], nums_sorted[r]])
                    while l < r and nums_sorted[l+1] == nums_sorted[l]:
                        l += 1
                    while l < r and nums_sorted[r-1] == nums_sorted[r]:
                        r -= 1
                    l += 1
                    r -= 1
                else:
                    r -= 1

        return ret
