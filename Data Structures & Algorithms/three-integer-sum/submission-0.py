class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]: # avoid duplicates in the solution set
                i += 1
                continue
            j, k = i+1, len(nums)-1 # j is NOT from 0 since the elements before i are already checked
            target = 0 - nums[i]

            while j < k:
                cur_sum = nums[j] + nums[k]
                if cur_sum == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]: # don't reverse the order of this conditions: nums[j+1] will be interpreted first and could generate out-of-bounds error
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1 # increment/decrement after findind a triplet too
                    k -= 1
                elif cur_sum < target and j < k:
                    j += 1
                elif cur_sum > target and j < k:
                    k -= 1
        
        return ans

