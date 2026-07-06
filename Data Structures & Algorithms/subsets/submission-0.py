class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return all possible subsets: backtrack
        # must not contain duplicates
        # time: O(2^n * n)
        # space: O(n) (not O(logn): the deepest path selects all n elements, so the call stack reaches depth n

        answer = []
        current = []
        def backtrack(start, current):
            # termination condition: none
            answer.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()
        
        backtrack(0, current)
        return answer
        
