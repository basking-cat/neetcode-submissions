class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # using sliding window because there is a condition(successive same characters) and we're looking at the string from left to right
        # find the character that appears the most in the current window and substract the occurrence count from the length of the window
        # if the result is less than k, we know that we can set the whole length of the current window to the max_len
        # also we keep track of the longest repeating character so far
        # we have to store the characters and their counts

        l = 0
        max_len = 0
        max_freq = 0
        hashmap = {}

        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            max_freq = max(max_freq, hashmap[s[r]])
            length = r - l + 1
            if length - max_freq <= k:
                max_len = max(max_len, length)
            else:
                while length - max_freq > k and l <= r:
                    hashmap[s[l]] -= 1
                    max_freq = max(hashmap.values()) if hashmap else 0 # don't forget to update max_freq
                    l += 1
                    # hashmap[s[l]] -= 1 # the order matters!!!!! in this way, s[l] is the next character to the one we want to update
                    length = r - l + 1 # don't forget to update the length too

        return max_len
    # time: O(n)
    # space: O(m) (m is the number of all the characters that appear in the string. in this case the space complexity can be considered O(1))
            
            

