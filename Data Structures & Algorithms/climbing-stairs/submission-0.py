class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        two_step_before = 1
        one_step_before = 2

        for i in range(3, n+1):
            current = two_step_before + one_step_before
            two_step_before = one_step_before
            one_step_before = current

        return one_step_before

    def climbStairsWithSpaceN(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

        # time: O(n)
        # space: O(n)