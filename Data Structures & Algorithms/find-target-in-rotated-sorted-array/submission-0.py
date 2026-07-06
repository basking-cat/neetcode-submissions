class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # split the array in half
        #   - compare the mid element with the first and last elements
        #   - choose one half in which mid and first/last elements are in ascending order
        # one of those two is sorted in ascending order
        # if the target is larger/less than the last/first val, do the same thing in the other half
        # otherwise, repeat splitting the array until we find the target val

        right = len(nums) - 1
        left = 0

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while left < right: # left side variant
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1 # left side variant: move forward only one of left or right
                else:
                    right = mid
            else:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid # left side variant: move forward only one of left or right
                else:
                    left = mid + 1
        
        if nums[left] == target: # need this for when it finishes with left == right
            return left


        # while left <= right: # both sides variant
        #     mid = left + (right - left) // 2
        #     if nums[mid] == target:
        #         return mid

        #     if nums[mid] < nums[right]:
        #         if nums[mid] < target and target <= nums[right]:
        #             left = mid + 1 # both sides variant: not just 'mid' to prevent infinite loop
        #         else:
        #             right = mid - 1
        #     else:
        #         if nums[left] <= target and target < nums[mid]:
        #             right = mid - 1 # both sides variant: not just 'mid' to prevent infinite loop
        #         else:
        #             left = mid + 1

        return -1