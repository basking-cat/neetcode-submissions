class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> int:
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1 # (right - 1) - (left + 1) + 1

        for i in range(len(s)):
            len_odd = expand_around_center(i, i)
            len_even = expand_around_center(i, i+1)
            max_len = max(len_odd, len_even)

            if max_len > (end - start): # Avoids +1 to handle the initial 1-character case correctly while ensuring we only update for a strictly longer palindrome
                start = i - (max_len - 1)//2
                end = i + max_len//2

        return s[start:end+1]