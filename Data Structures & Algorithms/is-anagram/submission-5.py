class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first of all inputs are rejected if lengths don't match
        if len(s) != len(t):
            return False
        # time complexity of the sorting algorithm in python: O(nlogn)
        return sorted(s) == sorted(t)

    # time complexity: O(nlogn + mlogm) because of the sorting algorithm
    # space complexity: O(1) or O(n) (depends on the sorting algorithm)

    # unless we know that n dominates m, we must keep both terms