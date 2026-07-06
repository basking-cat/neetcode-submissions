from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s = Counter(s)
        c_t = Counter(t)
    
        if c_s == c_t:
            return True
        return False