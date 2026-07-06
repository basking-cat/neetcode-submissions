class Solution:
    def isValid(self, s: str) -> bool:
        # use stack and hashmap
        # if the character we're currently looking at is a closing bracket, we look up the hashmap and compare it to stack.pop()
        # if stack is not empty at the end or empty before reading all the characters, the input is not valid
        # if the length of the string is odd, return false immediately
        
        if len(s)%2 != 0:
            return False

        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c not in hashmap: # append open brackets
                stack.append(c)
            else:
                if not stack or stack.pop() != hashmap[c]:
                    return False

        return not stack
    # time: O(n)
    # space: O(n)
        
