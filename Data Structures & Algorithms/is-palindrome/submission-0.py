class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i <= j:
            while not s[i].isalnum() and i < j: # add 'i < j' to prevent the pointer from going out of bounds
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1

            if not s[i].lower() == s[j].lower():
                return False

            i += 1
            j -= 1
        return True
    # time: O(n)
    # space: O(1)

class SolutionBruteForce:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    
    # time: O(n)
    # space: O(n)