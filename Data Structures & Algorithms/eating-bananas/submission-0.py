class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the ith pile has piles[i] bananas
        # bananas-per-hour eating speed of k
        # binary search between 1 and max(piles)
        # min hour: when k = max(piles)
        # max hour: when k = 1

        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h: # this condition includes "="
                right = mid
            else:
                left = mid + 1

        return left