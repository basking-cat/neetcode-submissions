class Solution:
    def maxArea(self, height: List[int]) -> int:
        # use two-pointer
        # increment/decrement the indices so that the height of the next index will be taller
        # update the maximum amount when the amount is bigger than that
        # if the next amount is bigger, that happens only when you replace the shorter line with a taller one

        l, r = 0, len(height)-1
        maximum = 0

        while l < r:
            h_l, h_r = height[l], height[r]
            shorter = min(height[l], height[r])
            maximum = max(maximum, (r - l)*shorter)

            if h_l < h_r:
                while l < r and shorter > height[l+1]:
                    l += 1
                l += 1
            else:
                while l < r and shorter > height[r-1]:
                    r -= 1
                r -= 1
        
        return maximum
    # time: O(n)
    # space: O(1)