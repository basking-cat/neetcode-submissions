class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window algorithm & hashmap to check duplicates
        # two pointers:
        #   - one stays until there's a duplicate in the substring
        #   - one moves further
        # edge cases:
        #   - length 0 or 1: return 0 or 1
        
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        max_len = 1
        hashmap = {}
        l, r = 0, 1
        hashmap[s[l]] = 1
        while r < len(s):
            while s[r] in hashmap:
                del hashmap[s[l]]
                l += 1
            hashmap[s[r]] = r
            max_len = max(max_len, r-l+1)
            r += 1

        return max_len