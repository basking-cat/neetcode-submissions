class Solution:
    def countSubstrings(self, s: str) -> int:
        count, count_odd, count_even = 0, 0, 0
        def expand(left: int, right: int) -> int:
            cnt_local = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                cnt_local += 1
            return cnt_local

        for i in range(len(s)):
            count_odd = expand(i, i)
            count_even = expand(i, i+1)

            count += count_odd + count_even

        return count