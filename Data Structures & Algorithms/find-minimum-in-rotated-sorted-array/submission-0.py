class Solution:
    def findMin(self, nums: List[int]) -> int:
        # compare the middle element with the rightmost element
        # if the middle is bigger, the minimum is in the right half
        # else, it's in the left
        # repeat
        # time: O(logn), space: O(1)

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1 # mid can't be the answer in this case so we move left to mid + 1
            else:
                right = mid # NG: "right = mid - 1" since mid can be the minimum element
                # only in this case mid could be the answer
        return nums[right] 
        # the loop stops when left == right
        # we can't return mid here because it won't be calculated after the loop stops