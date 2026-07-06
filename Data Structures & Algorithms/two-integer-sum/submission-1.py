class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a hash set that stores all the values in nums
        # if target - nums[i] exists in the hash set, return the pair
        # indexes must be stored too to check i != j, so it has to be a hash set and not a set
        hashset = {}
        for i in range(len(nums)):
            hashset[nums[i]] = i
        
        print(hashset)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashset and hashset[diff] != i:
                return [min(i, hashset[diff]), max(i, hashset[diff])]

        
            