class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window algorithm & a set/hashmap to check duplicates
        # two pointers:
        #   - one stays until there's a duplicate in the substring
        #   - one moves further (use for & enumerate)
        # edge cases:
        #   - length 0 : return 0
        
        # --- hashmap solution ---
        if len(s) == 0:
            return 0

        hashmap = {}
        max_len = 0
        l = 0
        for i, ch in enumerate(s):
            if ch in hashmap and hashmap[ch] >= l: # ignore characters out of the window
                l = hashmap[ch] + 1
            hashmap[ch] = i
            max_len = max(max_len, i-l+1)

        return max_len

        # --- set solution ---
        # max_len = 0
        # seen = set()
        # l, r = 0, 0
        # while r < len(s):
        #     while s[r] in seen:
        #         seen.remove(s[l])
        #         l += 1
        #     seen.add(s[r])
        #     max_len = max(max_len, r-l+1)
        #     r += 1

        # return max_len