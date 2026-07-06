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
            rest = target - nums[i]
            if rest in hashset and hashset[rest] != i:
                return [min(i, hashset[rest]), max(i, hashset[rest])]
            