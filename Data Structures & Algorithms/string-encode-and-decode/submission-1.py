class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        # using while because the step size is non-uniform
        # we need to jump the pointer (i) forward by a variable amount after parsing the length of each string
        i=0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#': # the pointer j stops exactly at the delimiter
                j += 1
            
            # extract the actual length of the next string
            length = int(s[i:j]) # from i to j-1
            i = j + 1 # start of a string
            j = i + length # end of a string
            res.append(s[i:j]) 
            i = j # forward the pointer i to the start of the next encoded block

        return res
        