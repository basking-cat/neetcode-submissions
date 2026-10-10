class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window of a length of s1

        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)
        l, r = 0, len(s1) - 1
        window = Counter(s2[l:r+1])

        while r < len(s2):
            if window == s1_counter:
                return True
            
            if r + 1 < len(s2):
                r += 1
                l += 1
            else: break # you need this because it will cause an infinite loop without this

            window[s2[r]] += 1
            left_char = s2[l-1]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

        return False