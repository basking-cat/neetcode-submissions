class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # move left & right pointers after comparing the target with the middle element

        left = 0
        right = len(nums) - 1

        while left <= right: # left and right can point the same element
            mid = (left + right) // 2 # update mid in while loop

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1