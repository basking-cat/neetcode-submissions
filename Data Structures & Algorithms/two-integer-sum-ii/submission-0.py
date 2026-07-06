class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two-pointer
        # if the sum of two numbers is less than the target, increment the smaller index by one
        # if larger than the target, decrement the larger index by one

        i, j = 0, len(numbers)-1
        while i < j:
            cur_sum = numbers[i] + numbers[j]
            if cur_sum == target:
                return [i+1, j+1]
            if cur_sum < target and i < j:
                i += 1
            if cur_sum > target and i < j:
                j -= 1

        # time: O(n)
        # space: O(1)