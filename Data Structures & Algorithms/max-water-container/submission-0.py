class Solution:
    def maxArea(self, height: List[int]) -> int:
        # use two-pointer
        # increment/decrement the indices so that the height of the next index will be higher
        # update the maximum amount when the amount is bigger than that
        # if the next amount is bigger, that's only when you replace the shorter line with a taller one

        l, r = 0, len(height)-1
        maximum = 0

        while l < r:
            shorter = height[l] if height[l] < height[r] else height[r]
            amount = (r - l)*shorter
            if amount > maximum:
                maximum = amount

            if shorter == height[l]:
                while l < r and shorter > height[l+1]:
                    l += 1
                l += 1
            if shorter == height[r]:
                while l < r and shorter > height[r-1]:
                    r -= 1
                r -= 1
        
        return maximum