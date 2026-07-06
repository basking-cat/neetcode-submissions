class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # finding all unique combinations using backtrack
        # time: O(n^(t/m)), total nodes in the recursion tree
        #   - at each node we have up to n choices, and the max depth is t/m
        # space: O(t/m), max recursion depth 
        #   - occurs when we repeatedly choose the smallest candidate until the sum reaches the target
        # (t: target, m: minimum value in candidates)
        answer = []
        current = []
        rem = target

        def backtrack(start, current, rem):
            # base case: valid combination found
            if rem == 0:
                answer.append(current[:])
                return 
            # base case: target exceeded, prevent further recursion
            if rem < 0:
                return
                
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, rem-candidates[i])
                current.pop()

        backtrack(0, current, target)
        return answer