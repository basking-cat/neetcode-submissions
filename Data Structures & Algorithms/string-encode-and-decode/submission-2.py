class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            start = i

            while s[i] != '#':
                i += 1

            length = int(s[start:i])
            i += 1
            res.append(s[i:i+length])
            i += length

        return res

            