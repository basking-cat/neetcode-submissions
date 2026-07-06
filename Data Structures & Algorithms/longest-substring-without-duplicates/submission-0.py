class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using sliding window because we need two pointers starting from the beginning of the string, one stays until the condition is broken and one moves further to check if we include another character in each step
        # we need to store the characters we've seen to check the condition (duplicates)
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l, r = 0, 1 
        max_len = 1
        hashmap = {}
        hashmap[s[l]] = l

        while r < len(s):
            while s[r] in hashmap:
                del hashmap[s[l]]
                l += 1
                # l = r  # we might miss possible substrings in this way
                # hashmap = {}
            hashmap[s[r]] = r
            max_len = max(max_len, r-l+1)

            r += 1
        
        return max_len